from flask import Flask, Response

app = Flask(__name__)

@app.route('/<path:filepath>')
def serve_file(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    return Response(content, mimetype='text/plain')

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=39994, debug=True)