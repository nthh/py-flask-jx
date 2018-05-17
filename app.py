from flask import Flask
app = Flask(__name__)

PORT = 8080

@app.route('/')
def hello():
    return "Hello World PR!"

@app.route('/test')
def test():
    return "testing"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
