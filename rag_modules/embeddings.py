import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def embed_chunks(chunks: list[str]) -> list[list[float]]:
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=chunks,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT"
        ),
    )
    return [e.values for e in result.embeddings]

def embed_query(query: str) -> list[float]:
    result = client.models.embed_content(
        model='gemini-embedding-001',
        contents=[query],
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY"
        ),
    )
    return result.embeddings[0].values







