from fastapi import FastAPI

# FastAPI object
app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Hello world"}


# Path parameter
# http://127.0.0.1:8000/about/Ram/22
@app.get("/about/{name}/{age}")
def about(name,age):
    return {"message": f"My name is {name} and age is {age}"}

# Ouery parameter
# http://127.0.0.1:8000/about?name=Ram&age=21
@app.get("/about")
def about(name,age):
    return {"message": f"My name is {name} and age is {age}"}

# Pydantic
# pip install pydantic

from pydantic import BaseModel

class User(BaseModel):
    name:str
    email:str
    age:int

@app.post("/information")
def information(user:User):
    return user

# status code
# 200 - Success
# 422 - Unprocessable Entity
# 404 - Not found

# CURD : 
# user create
# get particular
# particular user update
# particular delete