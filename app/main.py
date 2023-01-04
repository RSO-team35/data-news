from typing import List
from fastapi import Depends, FastAPI, HTTPException, status, Response
from fastapi.responses import JSONResponse
from . import utility
import time 


description = "Service for getting and collecting tech news"
tags_metadata = [
    {
        "name": "news",
        "description": "Gets interesting news"
    }
]


app = FastAPI(title="News collector", description=description, openapi_tags=tags_metadata, docs_url="/openapi")


@app.get("/news/{product_name}/", tags=["news"])
def get_news(product_name: str):
    """
    Gets news linked to product
    """
    news = utility.get_news(product_name)
    return JSONResponse(content=news)

