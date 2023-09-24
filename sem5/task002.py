from enum import Enum
from typing import Optional
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel


app = FastAPI()


movies = []


class Genre(Enum):
    BOEVIK = "Боевик"
    FANTASTICA = "Фантастика"
    COMEDIA = "Комедия"


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: Genre


class MovieIn(BaseModel):
    title: str
    description: str
    genre: Genre


@app.get("/")
async def root():
    return {"message", "Hello, woirld"}


@app.get("/movies/{genre}", response_model=list[Movie])
async def get_movies(genre: Genre):
    result = []
    for movie in movies:
        if movie.genre == genre:
            result.append(movie)
    return result


@app.post("/movies/", response_model=Movie)
async def create_movie(new_movie: MovieIn):
    movies.append(
        Movie(id=len(movies) + 1, title=new_movie.title,
              description=new_movie.description, genre=new_movie.genre))
    return movies[-1]


# @app.put("/tasks/", response_model=Task)
# async def edit_task(task_id: int, new_task: TaskIn):

#     for i in range(0, len(tasks)):
#         if tasks[i].id == task_id:
#             current_task = tasks[task_id-1]
#             current_task.title = new_task.title
#             current_task.description = new_task.description
#             current_task.status = new_task.status
#             return current_task
#     raise HTTPException(status_code=404, detail="Task not found")


# @app.delete("/tasks/", response_model=dict)
# async def edit_task(task_id: int):
#     for i in range(0, len(tasks)):
#         if tasks[i].id == task_id:
#             tasks.remove(tasks[i])
#             return {"message": "Tasks was remove succesfully"}
#         raise HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    uvicorn.run("task002:app", host="127.0.0.1", port=8000, reload=True)
