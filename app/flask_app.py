from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def print_message():
    return "It's me and i am running on Openshift!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
