from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

todo=[]

class Todo(BaseModel):
    id:int
    title:str
    done:bool

@app.post('/create')
def AddTask(task:Todo)->Todo:
    todo.append(task)
    return task
@app.get('/read/')
def ShowTasks()->list:
    return todo

@app.get('/read/{did}')
def ShowTask(did:bool):
    for i in todo:
        if(i.done==did):
            return i
    return "error"

@app.put('/update/{id}')
def updateTask(id:int,updated_task:Todo):
    for index,i in enumerate(todo):
        if i.id==id:
            todo[index]=updated_task

@app.delete('/delete')
def DeleteTask(id:int):
    for i,index in todo:
        if(i.id==id):
            todo.pop(index)
