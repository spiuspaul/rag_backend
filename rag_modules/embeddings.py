import os
import voyageai

client = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))

def embed_chunks(chunks: list[str]) -> list[list[float]]:
    result = client.embed(chunks, model='voyage-2', input_type='document')
    return result.embeddings


