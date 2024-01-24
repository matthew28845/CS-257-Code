import psycopg2

conn = psycopg2.connect(host="localhost",
                        port=5432,
                        database="sigmondm",
                        user="sigmondm",
                        password="pies347cash")

cur = conn.cursor()
cur.execute("SELECT * FROM topcities WHERE city = 'Northfield';")
row = cur.fetchone()
if row is not None:
    print("Northfield is in the top 1,000 cities. Its location is (", row[3], ") and its latitude is (", row[4], ")")
else:
    print("Northfield is not in the top 1,000 cities. Very sad!")

cur.execute("SELECT * FROM topcities ORDER BY population DESC")
row = cur.fetchone()
print("The biggest city in the US is ", row[0],"and its population is", row[2])

cur.execute("SELECT * FROM topcities WHERE state = 'Minnesota' ORDER BY population ASC")
row = cur.fetchone()
print("The smallest city in Minnesota within the top 1000 is", row[0], "and its population is", row[2])

cur.execute("SELECT * FROM topcities ORDER BY longitude DESC")
row = cur.fetchone()
print("The farthest west US city in the top 1000 is", row[0], "and its population is", row[2])

cur.execute("SELECT * FROM topcities ORDER BY longitude ASC")
row = cur.fetchone()
print("The farthest east US city in the top 1000 is", row[0], "and its population is", row[2])

cur.execute("SELECT * FROM topcities ORDER BY latitude DESC")
row = cur.fetchone()
print("The farthest north US city in the top 1000 is", row[0], "and its population is", row[2])

cur.execute("SELECT * FROM topcities ORDER BY latitude ASC")
row = cur.fetchone()
print("The farthest south US city in the top 1000 is", row[0], "and its population is", row[2])

myState = input()
sql = "SELECT SUM(population) FROM topcities WHERE state ="
cur.execute(sql, myState)

cur.close()
conn.close()
