from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from document_converter.route import router as document_converter_router
from document_converter.auth import get_api_key
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Add authentication dependency to all routes
app.include_router(
    document_converter_router,
    prefix="",
    tags=["document-converter"],
    dependencies=[Depends(get_api_key)]
)
