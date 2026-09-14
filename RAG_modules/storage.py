import os
import psycopg2
from pgvector.psycopg2 import register_vector

#Setup connection
def get_connection():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    #pgvector's Python helper that teaches psycopg2 how to translate Python lists into Postgres's vector type automatically
    register_vector(conn) 
    return conn

#Store chunks 
def store_chunks(document_name:str, chunks: list[str], embeddings: list[list[float]]):
    conn = get_connection()
    curs = conn.cursor() #To issue SQL commands

    for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        curs.execute(
            """
            INSERT INTO document_chunks(document_name, chunk_text, chunk_index, embedding)
            VALUES(%s,%s,%s,%s)
            """
            (document_name, chunk, index, embedding)
        )

    conn.commit()
    curs.close()
    conn.close()

