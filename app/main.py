""" Main module of newscicd """
from fastapi import FastAPI, HTTPException

app = FastAPI()

NEWS = [
    {"id": 1, "headline": "No sun today in GC"},
    {"id": 2, "headline": "London imposes a 3 day only pizza diet"},
]


@app.get("/")
async def read_root():
    """API landing page"""
    return {"msg": "Welcome", "info": "Hit /news/{id} to get news article"}


@app.get("/news")
async def read_articles():
    """All news articles """
    return NEWS


@app.get("/news/{article_id}")
async def read_article(article_id: int):
    """User-facing GET article by ID"""
    article = await get_article(article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


async def get_article(article_id: int):
    """Filter article """
    for article in NEWS:
        if article["id"] == article_id:
            return article
