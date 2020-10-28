from fastapi import FastAPI

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return {"555555555555"}
@app.get("/b2s/{text}")
def bit2int(text:str):
    s = int(text[0])
    e = int(text[1:9], 2)
    f = [ int(x) for x in text[9:]]
    x = 1 + sum([ int(f[i])*2**(-(i+1)) for i in range(len(f)) ])
    result = (-1)**s * 2**(e-127) * x 
    return result