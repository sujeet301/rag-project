import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY was not found. Add it to the .env file."
    )

EMBEDDING_MODEL = os.getenv("GEMINI_EMBEDDING_MODEL", "gemini-embedding-2")
GENERATION_MODEL = os.getenv("GEMINI_GENERATION_MODEL", "gemini-3.8-flash")

client = genai.Client(api_key=API_KEY)


def create_embedding(text: str) -> list[float]:
    """Convert text to an embedding vector using Gemini."""
    result = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
    )

    if not result.embeddings:
        raise RuntimeError("Gemini returned no embedding.")

    return list(result.embeddings[0].values)
