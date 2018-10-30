from flask import Flask, request
from flask import jsonify

import vagalumeget

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'


@app.route('/vagalume/', methods=['GET'])
def vagalumetop15():
    # e.g: http://localhost:5000/vagalume/?artista='mamomas'
    # e.g: http://localhost:5000/vagalume/?artista='mamonas assassinas'
    bar = request.args.to_dict()
    artista = bar['artista']
    test = vagalumeget.gettop15(artista)
    test = jsonify(test)
    return test


@app.route('/vagalumemusic/', methods=['GET'])
def vagalumemusic():
    # e.g: http://localhost:5000/vagalume/?artista='mamomas'
    # e.g: http://localhost:5000/vagalume/?artista='mamonas assassinas'&limit=10
    bar = request.args.to_dict()
    artista = bar['artista']
    test = vagalumeget.gettop15(artista)
    test = jsonify(test)
    return test

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
