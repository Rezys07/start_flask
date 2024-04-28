from flask import Flask, url_for


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>hello world</h1>"

@app.route('/second')
def second():
    return "<h1>I'm here too my friend!</h1>"

@app.route('/user/<username>')
def profile(username):
    return f"{username}'s profile"

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('second'))
    print(url_for('second' , next="/"))
    print(url_for('profile' , username="rezy"))

#error route
@app.route('/<random_subject>')
def hello(random_subject):
    return f"<h1>error, the subject: {random_subject} doesn't exist here</h1>\n<h2>Try with other subject</h2>"

if __name__ == '__main__':
    app.run(debug=True)