from flask import Flask
app = Flask(__name__)


@app.route('/')
def awesome_function():
    return 'Learning DevOps is awesome!'