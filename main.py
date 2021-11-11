from flask import Flask
from werkzeug.exceptions import NotFound

app = Flask(__name__)

@app.route('/<string:name>/', methods=["GET", "POST"])
def wishes(name):
    return "Happy Birthday, " + name + "!"

@app.errorhandler(NotFound)
def handle_no_result_exception(error):
    '''Return a custom not found error message and 404 status code'''
    return {'message': 'Enter a name in the URL!'}, 404

if __name__ == '__main__':
    app.run()