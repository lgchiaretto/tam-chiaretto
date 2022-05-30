from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

app.debug = True

@app.route("/", methods=['GET'])
def index():
    return "hello world :)"
