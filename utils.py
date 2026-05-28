from database import get_connection


def store_embedding(content, embedding):
    conn = get_connection()

    cur = conn.cursor()

    query = """
    INSERT INTO document_embeddings (content, embedding)
    VALUES (%s, %s)
    """

    cur.execute(query, (content, embedding))

    conn.commit()

    cur.close()
    conn.close()

    print("Embedding stored successfully!")