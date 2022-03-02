from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello James again my friend - keep on pushing my man - do it!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
