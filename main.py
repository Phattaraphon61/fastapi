from fastapi import FastAPI
from pydantic import BaseModel
from numpy import sign
app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.
class eliminate(BaseModel):
    A:list
    b:list

class interpolation(BaseModel):
    x:int
    xi:list
    yi:list

class differentiation(BaseModel):
    h:float
    p:int

class integration(BaseModel):
    a:int
    b:int

class rootFinding(BaseModel):
    a:float
    b:float
    dx:float

@app.get("/")
def home():
    return {"8888"}
@app.get("/b2s/{text}")
def bit2int(text:str):
    s = int(text[0])
    e = int(text[1:9], 2)
    f = [ int(x) for x in text[9:]]
    x = 1 + sum([ int(f[i])*2**(-(i+1)) for i in range(len(f)) ])
    result = (-1)**s * 2**(e-127) * x 
    return result