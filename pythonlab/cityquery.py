import psycopg2

conn = psycopg2.connect(host="localhost",
                        port=5432,
                        database="sigmondm",
                        user="sigmondm",
                        password="pies347cash")

cur = conn.cursor()
cur.execute("SELECT * FROM topcities WHERE city = 'Northfield';")
row = cur.fetchone()
if len(row) > 0:
    print("Northfield is in the top 1,000 cities. Its location is (", row[3], ") and its latitude is (", row[4], ")")
else:
    print("Northfield is not in the top 1,000 cities. Very sad!")
conn.commit()

cur.close()
conn.close()
