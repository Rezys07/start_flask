from flask import Flask, url_for , render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ex002.html')

if __name__ == '__main__':
    app.run(debug=True)
