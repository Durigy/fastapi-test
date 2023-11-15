from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello")
async def hello():
    return {"message": "Hello To the ..."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", port=8000)
