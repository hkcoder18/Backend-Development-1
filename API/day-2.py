# Virtual Environmet

# commands to create virtual environment
# 1. python -m venv myenv -- to create virtual environment
# 2. myenv\Scripts\activate -- to activate virtual env

# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI

# creating object of FastAPI class.
app = FastAPI()

@app.get("/home") # endpoint -- api url
def home():
    return {"message": "Hello World!!"}

@app.post("/about") # endpoint
def about(name:str,age:int):
    return {"message": f"My name is {name} and age is {age}"}

@app.post("/login")
def login(username:str,password:str):
    if username=="Ram" and password=="123":
        return {"message": "Login successfully"}
    return {"message": "Invalid Credentials"}


# python -m uvicorn API.day-2:app --reload
# to open swager-UI : http://127.0.0.1:8000/docs