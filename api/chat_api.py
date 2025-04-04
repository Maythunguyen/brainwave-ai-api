from fastapi import APIRouter
from schemas.chat_schemas import ChatRequest, ChatResponse
from services.openai_service import AIService

chat_router = APIRouter()
ai_service = AIService()

@chat_router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    print(f"📩 Received message: {request.message}")
    ai_reply = ai_service.get_ai_response(request.message)
    return ChatResponse(reply=ai_reply)

@chat_router.get("/test")
def test_route():
    return {"message": "Chat router is working"}
