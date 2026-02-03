# API - Application Programming interface

# Frontend - username:xyz & pass:124
# Forntend data == database data -- pass is wrong
# Database - username:xyz & pass:123

# GET - get data
# POST - data add. (Account creation)
# PUT - Update
# PATCH - Update
# DELETE - delete/remove

# CURD operations
# C - Creation
# U - Update
# R - Retirive (Get)/Read
# D - Delete/Remove


# Framework
# FastAPI : FastAPI is a framework that is used to built API's
# Django, Flask
# FastAPI is much easier than Django and Flask
# FastAPI is modern trending tech stack
# used in AI/ML

# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get('/data') #end-point
def show_data():
    return {"message" : "These is a get API"}

@app.get('/hello')
def hello():
    return {"message" : "Hello world!!"}

# commands to run 
# python -m uvicorn file_name:app --reload

# UI Format of API's
# http://127.0.0.1:8000/docs