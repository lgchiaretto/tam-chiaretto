from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

app.debug = True

@app.route("/", methods=['GET'])
def index():
    return "hello world :)"

@app.route("/pod", methods=['GET'])
def pod():
    return os.uname()
