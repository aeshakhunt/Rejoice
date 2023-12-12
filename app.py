from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List

app=FastAPI()


class input_schema(BaseModel):
    name:str
    decription:str

class output_schema(BaseModel):
    id:int
    name:str
    decription:str

fakedb=[]

@app.post("/" )
def item(input:input_schema):
    user={
        "name":input.name,
        "decription":input.decription,
        "id":len(fakedb)
    }
    fakedb.append(user)
    return fakedb

@app.get("/")
def read():
    return fakedb


    
    