import os
from fastapi import APIRouter, UploadFile, File
from pypdf import PdfReader
from rag_modules.chunking import chunk_text
from rag_modules.embeddings import embed_chunks
from rag_modules.storage import store_chunks 

router = APIRouter(prefix="/documents", tags=["documents"])
UPLOAD_DIR = "uploads"

@router.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    chunks = chunk_text(text)
    embeddings = embed_chunks(chunks)
    store_chunks(file.filename, chunks, embeddings)

    return {
        "filename": file.filename,
        "page_count": len(reader.pages),
        "text": text,
        "chunk_count": len(chunks)
    }







