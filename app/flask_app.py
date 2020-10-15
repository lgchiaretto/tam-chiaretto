from flask import Flask
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

@app.route('/databses', methods=['GET'])
def print_databases():
    db = mysql.connect(
        host = "mysql-57-rhel7.chiaretto.svc",
        user = "admin",
        passwd = "redhat"
    )

    cursor = db.cursor()

    ## executing the statement using 'execute()' method
    cursor.execute("SHOW DATABASES")

    ## 'fetchall()' method fetches all the rows from the last executed statement
    databases = cursor.fetchall() ## it returns a list of all databases present

    ## printing the list of databases
   return databases


if __name__ == '__main__':
    app.run(host='0.0.0.0')
