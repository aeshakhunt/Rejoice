from typing import Union,Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class mathoperation(BaseModel):
    num1 : Union[float,int]
    num2 : Union[float,int]
    num3 : Optional[None]

class mathresult(BaseModel):
    result : Union[float,int]

@app.post("/add",response_model=mathresult,status_code=201)
def addNumber(operation:mathoperation):
    result=operation.num1+operation.num2
    return {"result":result}

@app.post("/substract",response_model=mathresult,status_code=201)
def substractNumber(operation:mathoperation):
    result=operation.num1-operation.num2
    return {"result":result}

@app.post("/multi",response_model=mathresult,status_code=201)
def multiNumber(operation:mathoperation):
    result=operation.num1*operation.num2
    return {"result":result}

@app.post("/division",response_model=mathresult,status_code=201)
def divNumber(operation:mathoperation):
    result=operation.num1/operation.num2
    return {"result":result}
