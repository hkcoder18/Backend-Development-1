# To-Do-List mini project

# we can add Task
# we can see particular task
# we can update particular task
# we can delete delete particular task

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# We can stored our tasks
todos = []

# id
# tittle
# description
# completed

class ToDo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

class ToDoUpdate(BaseModel):
    title: str
    description: str
    completed: bool

@app.get('/')
def home():
    return {"message": "To-Do-List API's"}

@app.get("/tasks")
def get():
    """
        Used to get all tasks
    """
    return todos

@app.post('/task')
def create(todo: ToDo):
    """
        Used to add new task
    """
    print("Type : ",type(todo))
    todo_dict = todo.dict()
    todos.append(todo_dict)
    return {"message": "Task successfully added!!"}

@app.put('/todo/{id}/')
def update(id: int, updated: ToDoUpdate):
    for task in todos:
        if task["id"]==id:
            data = updated.dict()
            task.update(data)
            return {"message": "Task successfully updated!!"}
    else:
        raise HTTPException(status_code=400,detail="Tast not found")
    
@app.delete("/todo/{id}/")
def delete(id: int):
    for idx,task in enumerate(todos):
        if task["id"]==id:
            todos.pop(idx)
            return {"message": "Task successfully deleted!!"}
    else:
        return {"message": "Task not found or Already deleted!"}

    # 200 - sucess
    # 201 - sucess
    # 400 - bad request
    # 404 - not found
    # 500 - internal server error