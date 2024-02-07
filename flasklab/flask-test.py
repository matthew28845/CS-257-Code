import flask

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/add/<word1>/<word2>')
def my_addition(word1, word2):
    word1 = int(word1)
    word2 = int(word2)
    the_sum = word1 + word2
    the_string = "The sum is: " + the_sum;
    return the_sum

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'

if __name__ == '__main__':
    my_port = 5132
    app.run(host='0.0.0.0', port = my_port) 
