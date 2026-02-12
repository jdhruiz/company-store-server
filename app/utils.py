from db import get_connection

def query_db(query, params=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params or ())

    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    results = [dict(zip(columns, row)) for row in rows]

    cur.close()
    conn.close()

    return results
