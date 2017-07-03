<<<<<<< HEAD
from flask import *

app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html")


if __name__ == '__main__':
    app.run()
=======
from flask import *

app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html")


if __name__ == '__main__':
    app.run()
>>>>>>> df6e0d7a9a153ae19f9236bbc8b5e195ece4f816
