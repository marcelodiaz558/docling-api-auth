from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY_NAME = "X-API-Key"
API_KEY = os.getenv("API_KEY")
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

async def get_api_key(api_key_header: str = Depends(api_key_header)):
    if not API_KEY:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API Key not configured"
        )
    if not api_key_header == API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return api_key_header 