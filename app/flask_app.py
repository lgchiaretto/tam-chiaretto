from flask import Flask
from flask import jsonify
import time
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
    databases = cursor.fetchall() ## it returns a list of all databases present
    for database in databases
        alldbs.append(database)
    return jsonify(alldbs)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
