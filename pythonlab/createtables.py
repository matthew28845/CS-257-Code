import psycopg2

conn = psycopg2.connect(host="localhost",
        port=5432,
        database="sigmondm",
        user="sigmondm",
        password="pies347cash")

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS topcities;")
cur.execute("CREATE TABLE topcities (city TEXT, state TEXT, population LONG, latitude DOUBLE, longitude DOUBLE);")