from pydantic import BaseModel

class QueryRequest(BaseModel):
    document_name: str
    question: str