import psycopg2

conn = psycopg2.connect(host="localhost",
                        port=5432,
                        database="sigmondm",
                        user="sigmondm",
                        password="pies347cash")

cur = conn.cursor()
cur.execute("SELECT * FROM topcities WHERE city = 'Northfield';")
row = cur.fetchone()
if row.type is not None:
    print("Northfield is in the top 1,000 cities. Its location is (", row[3], ") and its latitude is (", row[4], ")")
else:
    print("Northfield is not in the top 1,000 cities. Very sad!")

cur.execute("SELECT * FROM topcities ORDER BY population DESC")
row = cur.fetchone()
print("The biggest city in the US is ", row[0], "and its population is", row[2])

cur.execute("SELECT * FROM topcities WHERE state = 'Minnesota' ORDER BY population ASC")

cur.close()
conn.close()
