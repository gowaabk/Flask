import logging
from fastapi import FastAPI


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


@app.get("/")
async def read_root():
    logger.info("Отработал GET запрос.")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# @app.post("/items/")
# async def create_item(item: Item):
#     logger.info('Отработал POST запрос.')
#     return item
