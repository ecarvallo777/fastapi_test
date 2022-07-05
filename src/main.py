import fastapi

from fastapi import FastAPI

app = FastAPI()


@app.get("/getPatent")
async def root():
    return {"message": "Hello PATENT"}
@app.get("/getId")
async def root():
    return {"message": "Hello ID"}