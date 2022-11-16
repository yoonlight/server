from typing import Union

from fastapi import FastAPI

from app.routers import items

app = FastAPI()

app.include_router(items.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
