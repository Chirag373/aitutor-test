import uvicorn
from fastapi import FastAPI
from api.routes import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
