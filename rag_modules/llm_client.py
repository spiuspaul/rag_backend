import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(question: str, context_chunks: list[list[float]]) -> str:
    context = "\n\n---\n\n".join(context_chunks)

    prompt = f"""Answer the question using only the context below
    If the context doesn't contain the answer, say so
    
    Context:
    {context}
    
    Question:{question}

    Answer:
    """
    response = client.chat.completions.create(
        messageS=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return response.choices[0].message.content