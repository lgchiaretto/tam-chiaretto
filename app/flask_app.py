from flask import Flask
import time
import socket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def print_message():
    return "It's me, Mario!!!"

@app.route('/healthcheck', methods=['GET'])
def print_helthcheck():
    return "ok"

@app.route('/pod', methods=['GET'])
def print_pod():
    return socket.gethostname()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
