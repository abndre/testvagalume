from flask import Flask, request
from flask import jsonify
import os
import vagalumeget

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/vagalume/', methods=['GET'])
def vagalumemusic():
    # e.g: http://localhost:5000/vagalume/?artista='mamonas assassinas'&limit=10
    bar = request.args.to_dict()
    artista = bar['artista']
    limit	= bar['limit']
    test = vagalumeget.getmusics(artista,limit)
    test = jsonify(test)
    return test

@app.route('/vagalumetop/', methods=['GET'])
def vagalumetop15():
    # e.g: http://localhost:5000/vagalumetop/?artista='mamomas'
    bar = request.args.to_dict()
    artista = bar['artista']
    test = vagalumeget.gettop15(artista)
    test = jsonify(test)
    return test

@app.route('/vagalumeletra/', methods=['GET'])
def vagalumeletra():
    # e.g: http://localhost:5000/vagalumeletra/?artista='mamomas'&letra='Jumento Celestino'
    bar = request.args.to_dict()
    artista = bar['artista']
    letra  = bar['letra']
    test = vagalumeget.getletra(artista,letra)
    test = jsonify(test)
    return test

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
