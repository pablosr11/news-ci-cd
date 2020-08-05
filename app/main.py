from fastapi import FastAPI, HTTPException

app = FastAPI()

NEWS = [
    {
        "id":1,
        "headline":"No sun today in GC"
    },
    {
        "id":2,
        "headline":"London imposes a 3 day only pizza diet"
    }
]


@app.get("/")
async def read_root():
    return {"msg": "Welcome", "info":"Hit /news/{id} to get news article"}

@app.get("/news")
async def read_articles():
    return NEWS

@app.get("/news/{article_id}")
async def read_article(article_id: int):
    article = await get_article(article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

async def get_article(id:int):
    for article in NEWS:
        if article["id"] == id:
            return article