from fastapi import FastAPI

from .parser import EksiParser

app = FastAPI()

eksi = EksiParser()


@app.get("/")
def read_root():
    return {"name": "eksi-api", "version": "0.0.1-pretest"}


@app.get("/topic/search/{query}")
def search_topic(query: str, page: int = 1):
    return eksi.search_topic(query, page)


@app.get("/entries/search/{query}")
def search_topic_with_entries(query: str, page: int = 1):
    topic = eksi.search_topic(query, page)
    print(topic)
    topic["entries"] = eksi.get_entries_from_url(topic["url"])
    return topic


@app.get("/topic/trending")
def get_trending_topics():
    return eksi.get_trending_topics()


@app.get("/topic/trending/details")
def get_trending_topic_details():
    topics = eksi.get_trending_topics()
    for topic in topics:
        topic["details"] = eksi.get_topic(topic["url"])
    return topics


@app.get("/entry/trending")
def get_trending_entries():
    topics = eksi.get_trending_topics()
    for topic in topics:
        topic["entries"] = eksi.get_entries_from_url(topic["url"])
    return topics


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
