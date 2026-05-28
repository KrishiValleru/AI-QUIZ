import psycopg2


def get_connection():
    conn = psycopg2.connect(
        dbname="quizdb",
        user="Krishi.Valleru",
        password="",
        host="localhost",
        port="5432"
    )

    return conn