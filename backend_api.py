import os
import logging
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from openai import AsyncOpenAI 

# Configure exact logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Make sure the API Key is loaded in your environment settings
# os.environ["OPENAI_API_KEY"] = "your_key"
client = AsyncOpenAI() 

class ChatRequest(BaseModel):
    query: str
    user_id: str

@app.post("/query")
async def chat_endpoint(request: Request, payload: ChatRequest):
    logger.info("--- [BACKEND LOG] Received request at /query ---")
    
    # 1. Log Raw Request Data
    try:
        raw_body = await request.body()
        logger.info(f"Raw Request Body: {raw_body.decode('utf-8')}")
    except Exception as e:
        logger.error(f"Failed to read raw body: {str(e)}")

    logger.info(f"Parsed Payload -> query: '{payload.query}', user_id: '{payload.user_id}'")

    # 2. Validate input
    if not payload.query or not payload.query.strip():
        logger.warning("--- [BACKEND ERROR] Empty query received ---")
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    try:
        logger.info("--- [BACKEND LOG] Calling AI Model ---")
        
        # 3. AI API Call
        chat_completion = await client.chat.completions.create(
            model="gpt-3.5-turbo", # Adapt for GPT-4 or groq versions (llama3)
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant focusing on medical awareness. Keep answers concise."},
                {"role": "user", "content": payload.query}
            ],
            temperature=0.7,
            max_tokens=512
        )
        
        # 4. Extract and Log AI Response
        ai_response_text = chat_completion.choices[0].message.content
        logger.info(f"--- [BACKEND LOG] Strict AI Response Received ---")
        logger.info(f"Tokens Usage: {getattr(chat_completion, 'usage', 'N/A')}")
        logger.info(f"Output text: {ai_response_text}")

        # 5. Return EXACT expected format
        return {"response": ai_response_text}

    except Exception as e:
        # 6. Log exact failure point in AI logic to avoid silent failures
        logger.error("--- [BACKEND CRITICAL ERROR] AI Generation failed ---", exc_info=True)
        raise HTTPException(status_code=500, detail=f"AI Engine Error: {str(e)}")
