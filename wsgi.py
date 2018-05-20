from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World this is a new test!"

if __name__ == "__main__":
    application.run()
