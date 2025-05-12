from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Dict, Any
import os

from src.handlers.slack_handler import SlackHandler
from src.greg.agent import GregAI

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "static")
templates_dir = os.path.join(current_dir, "templates")

app = FastAPI(
    title="Greg - Level 1 Oncall Bot",
    version="0.1.0",
    description="AI-powered oncall assistant with Slack-like interface"
)

# Mount static files directory
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Initialize templates
templates = Jinja2Templates(directory=templates_dir)

# Initialize our components
slack_handler = SlackHandler()
greg_ai = GregAI()

class MessageEvent(BaseModel):
    """Message event model"""
    user: str
    text: str
    channel: str

@app.get("/", response_class=HTMLResponse)
async def get_chat_interface(request: Request):
    """Serve the chat interface"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/message")
async def handle_message(event: MessageEvent):
    """Handle incoming messages from the web interface"""
    
    # 1. Receive and process the message
    message = slack_handler.receive_message(
        user=event.user,
        text=event.text,
        channel=event.channel
    )
    
    # 2. Process message with Greg AI
    response = greg_ai.process_message(message.to_dict())
    
    # 3. Send response back
    slack_response = slack_handler.send_message(
        channel=event.channel,
        text=response,
        thread_ts=message.timestamp
    )
    
    return {"status": "ok", "response": slack_response}

@app.get("/health")
async def health_check():
    """Simple health check endpoint"""
    return {"status": "healthy", "version": "0.1.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)