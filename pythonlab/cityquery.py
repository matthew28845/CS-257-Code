import psycopg2

# Connect to the SQL server hosted on the local machine
conn = psycopg2.connect(host="localhost",
                        port=5432,
                        database="sigmondm",
                        user="sigmondm",
                        password="pies347cash")

cur = conn.cursor()

# See if Northfield is in the list, and if so tell its coordinates
cur.execute("SELECT * FROM topcities WHERE city = 'Northfield';")
row = cur.fetchone()
if row is not None:
    print("Northfield is in the top 1,000 cities. Its location is (", row[3], ") and its latitude is (", row[4], ")")
else:
    print("Northfield is not in the top 1,000 cities. Very sad!")

# List the biggest city in the US
cur.execute("SELECT * FROM topcities ORDER BY population DESC")
row = cur.fetchone()
print("The biggest city in the US is ", row[0],"and its population is", row[2])

#List the smallest city in Minnesota within the top 1000
cur.execute("SELECT * FROM topcities WHERE state = 'Minnesota' ORDER BY population ASC")
row = cur.fetchone()
print("The smallest city in Minnesota within the top 1000 is", row[0], "and its population is", row[2])

#List the westernmost city in the top 1000
cur.execute("SELECT * FROM topcities ORDER BY longitude ASC")
row = cur.fetchone()
print("The farthest west US city in the top 1000 is", row[0], "and its population is", row[2])

#List the easternmost city in the top 1000
cur.execute("SELECT * FROM topcities ORDER BY longitude DESC")
row = cur.fetchone()
print("The farthest east US city in the top 1000 is", row[0], "and its population is", row[2])

#List the northernmost city in the top 1000
cur.execute("SELECT * FROM topcities ORDER BY latitude DESC")
row = cur.fetchone()
print("The farthest north US city in the top 1000 is", row[0], "and its population is", row[2])

#List the southernmost city in the top 1000
cur.execute("SELECT * FROM topcities ORDER BY latitude ASC")
row = cur.fetchone()
print("The farthest south US city in the top 1000 is", row[0], "and its population is", row[2])

# Let the user input a state, and then print out the sum of the population of the top cities in that state.
myState = str(input("Enter a state to see the sum of its population: "))
sql = "SELECT SUM(population) FROM topcities WHERE state = (%s);"
cur.execute(sql, myState)

cur.close()
conn.close()
