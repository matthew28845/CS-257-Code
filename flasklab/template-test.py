from flask import Flask
from flask import render_template, redirect, request, url_for
import random
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(host="localhost",
                        port=5432,
                        database="sigmondm",
                        user="sigmondm",
                        password="pies347cash")

cur = conn.cursor()


@app.route('/', methods=("GET", "POST"))
def welcome():
    if request.method == 'POST':
        state = request.form['stateinput']
        url_to_redirect = "/pop/"+state
        return redirect(url_to_redirect)
    return render_template("index.html")

@app.route('/rand/<low>/<high>')
def rand(low, high):
    # Input values that come from a URL (i.e., @app.route)
    #   are always strings so I need to convert the type to int
    low_int = int(low)
    high_int = int(high)

    num = random.randint(low_int, high_int)
    return render_template("random.html", randNum=num)


@app.route('/pop/<state>')
def pop(state):
    my_state = state
    cities_list = list()
    cur.execute("SELECT * FROM topcities WHERE state = %s ORDER BY population DESC FETCH FIRST 5 ROWS ONLY;",
                [my_state], )
    for i in range(5):
        row = cur.fetchone()
        cities_list.append(row)
    return render_template("pop.html", city1=cities_list[0], city2=cities_list[1], city3=cities_list[2],
                           city4=cities_list[3], city5=cities_list[4])


if __name__ == '__main__':
    my_port = 5132
    app.run(host='0.0.0.0', port=my_port)
