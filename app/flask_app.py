from flask import Flask
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def print_message():
    return "It's me, Mario!!!"

@app.route('/healthcheck', methods=['GET'])
def print_helthcheck():
    time.sleep(30)
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
