import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! This is a test to make sure deployment is functional.'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
