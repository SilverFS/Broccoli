from flask import Flask, render_template
from waitress import serve
import random


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def randomshit():
    randomshitt = random.randint(1, 137)
    return render_template('random.html', randomshitt=randomshitt)


if __name__ == "__main__":
    #app.run(host='0.0.0.0', port='9001', debug=True)
    serve(app, host='0.0.0.0', port=9001)
