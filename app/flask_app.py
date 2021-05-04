from flask import Flask
from flask import jsonify
from flask import request
import time
import subprocess
import socket
import mysql.connector as mysql

app = Flask(__name__)

@app.route('/', methods=['GET'])
def print_message():
    return "It's me, Mario!"

@app.route('/healthcheck', methods=['GET'])
def print_helthcheck():
    return "ok"

@app.route('/pod', methods=['GET'])
def print_pod():
    return socket.gethostname()

@app.route('/version', methods=['GET'])
def print_pod():
    return os.environ.get('APP_VERSION')

@app.route('/secret', methods=['GET'])
def print_pod():
    return os.environ.get('APP_SECRET')

@app.route('/help', methods=['GET'])
def print_pod():
    return """GET /
              GET /databases
              GET /secret
              GET /version
              GET /pod
              GET /healthcheck"""

@app.route('/databases', methods=['GET'])
def print_databases():
    db = mysql.connect(
        host = "mysql-57-rhel7.chiaretto.svc",
        user = "admin",
        passwd = "redhat"
    )
    alldbs = []
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    for database in databases:
        alldbs.append(database)
    return jsonify(alldbs)

@app.route('/crash', methods=['GET'])
def ExitScript():
    subprocess.Popen("^D")
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
