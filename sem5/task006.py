from enum import Enum
from typing import Optional
from fastapi import FastAPI, HTTPException, Request, requests
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from pydantic import BaseModel


app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


class UserOut(BaseModel):
    id: int
    name: str
    email: str


class UserIn(BaseModel):
    name: str
    email: str
    password: str


class User(UserIn):
    id: int


for i in range(10):
    users.append(
        User(id=i+1, name=f'name{i+1}', email=f'email{i+1}@mail.ru', password="123"))


@app.get("/")
async def root():
    return {"message", "Hello, woirld"}


@app.get("/users/", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


if __name__ == "__main__":
    uvicorn.run("task006:app", host="127.0.0.1", port=8000, reload=True)
