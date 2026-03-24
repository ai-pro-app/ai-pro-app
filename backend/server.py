from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()
api_router = APIRouter(prefix="/api")

REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

headers = {
    "Authorization": f"Token {REPLICATE_API_TOKEN}",
    "Content-Type": "application/json"
}

@api_router.get("/")
async def root():
    return {"message": "Hello World"}

# CHAT
@api_router.post("/chat")
async def chat(data: dict):
    prompt = data.get("message")

    res = requests.post(
        "https://api.replicate.com/v1/predictions",
        headers=headers,
        json={
            "version": "meta/llama-2-70b-chat",
            "input": {"prompt": prompt}
        }
    )
    return res.json()

# IMAGE
@api_router.post("/generate-image")
async def generate_image(data: dict):
    prompt = data.get("prompt")

    res = requests.post(
        "https://api.replicate.com/v1/predictions",
        headers=headers,
        json={
            "version": "stability-ai/sdxl",
            "input": {"prompt": prompt}
        }
    )
    return res.json()

# VIDEO
@api_router.post("/generate-video")
async def generate_video(data: dict):
    prompt = data.get("prompt")

    res = requests.post(
        "https://api.replicate.com/v1/predictions",
        headers=headers,
        json={
            "version": "zeroscope",
            "input": {"prompt": prompt}
        }
    )
    return res.json()

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
