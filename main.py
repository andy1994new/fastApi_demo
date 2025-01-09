from mylib.logic import wiki
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_index():
    return wiki()