import flask
import psycopg2

app = flask.Flask(__name__)
conn = psycopg2.connect(host="localhost",
                        port=5432,
                        database="sigmondm",
                        user="sigmondm",
                        password="pies347cash")

cur = conn.cursor()
#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string
@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'
@app.route('/add/<word1>/<word2>')
def my_addition(word1, word2):
    word1 = int(word1)
    word2 = int(word2)
    the_sum = word1 + word2
    the_sum = str(the_sum)
    the_string = "The sum is: " + the_sum;
    return the_string

@app.route('/pop/<abbrev>')
def my_pop(abbrev):
    my_abbreviation = abbrev
    cur.execute("SELECT * FROM statepopulations WHERE code = %s", [my_abbreviation],)
    row = cur.fetchone()
    my_population = str(row[2])
    the_string = "The population of " + str(row[1]) + " is: " + my_population;
    return the_string


if __name__ == '__main__':
    my_port = 5132
    app.run(host='0.0.0.0', port = my_port) 
