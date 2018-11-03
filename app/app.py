from flask import Flask, request
from flask import jsonify
import os
import vagalumeget
from flask_sqlalchemy import SQLAlchemy

#este seria o link do banco criado pelo heroku
postgreelink = 'postgres://cpjtqudnnygdji:c65440f4b0d30763bb3ef68f66eddf9a2765d29f79cadfdb362f19c683678a01@ec2-75-101-138-26.compute-1.amazonaws.com:5432/d8ggrgf7chi7ca'
app.config['SQLALCHEMY_DATABASE_URI'] = postgreelink
db = SQLAlchemy(app)

app = Flask(__name__)


'''
Esta rota foi deixada apenas para apresentacao da aplicacao
'''
@app.route('/')
def hello_world():
    return 'Sendo you requisition'


'''
As API abaixo enviam a requisicao para outro arquivo 'vagalumeget.py'
em suma aqui e feito o parse da url com:
nome do artista
letra de musica
limite de musicas
'''


'''
nesta url deve ser enviado o nome e o limit de musicas a serem requisitadas
'''
@app.route('/vagalume/', methods=['GET'])
def vagalumemusic():
    # e.g: http://localhost:5000/vagalume/?artista='mamonas assassinas'&limit=10
    bar = request.args.to_dict()
    artista = bar['artista']
    limit	= bar['limit']
    test = vagalumeget.getmusics(artista,limit)
    test = jsonify(test)
    return test

'''
nesta url deve ser enviado o nome do artista e sera retornado as top15 musicas
'''
@app.route('/vagalumetop/', methods=['GET'])
def vagalumetop15():
    # e.g: http://localhost:5000/vagalumetop/?artista='mamomas'
    bar = request.args.to_dict()
    artista = bar['artista']
    test = vagalumeget.gettop15(artista)
    test = jsonify(test)
    return test


'''
nesta url deve ser incerido o nome do artista e a musica desejada
'''
@app.route('/vagalumeletra/', methods=['GET'])
def vagalumeletra():
    # e.g: http://localhost:5000/vagalumeletra/?artista='mamomas'&letra='Jumento Celestino'
    bar = request.args.to_dict()
    artista = bar['artista']
    letra  = bar['letra']
    test = vagalumeget.getletra(artista,letra)
    test = jsonify(test)
    return test


'''
funcao para inicio
'''
if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
