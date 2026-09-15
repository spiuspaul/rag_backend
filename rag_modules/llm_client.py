import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_answer(question: str, context_chunks: list[list[float]]) -> str:
    context = "\n\n---\n\n".join(context_chunks)

    prompt = f"""Answer the question using only the context below
    If the context doesn't contain the answer, say so
    
    Context:
    {context}
    
    Question:{question}

    Answer:
    """
    response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=prompt
    )

    return response.text