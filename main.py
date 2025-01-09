from mylib.logic import wiki, wiki_search
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def get_index():
    return {"massage": "call /search or /wiki"}


@app.get("/search/{word}")
def search(word):
    return wiki_search(word)


@app.get("/wiki/{name}")
def get_wiki(name):
    return {"massage": wiki(name)}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
