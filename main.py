import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.chat_api import chat_router

def create_app() -> FastAPI:
    app = FastAPI(title="AI Chat App", version="0.1.0")

    # CORS config
    origins = [
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    def read_root():
        return {"message": "Welcome to the AI Chat App!"}

    app.include_router(chat_router, prefix="/api", tags=["Chat"])
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
