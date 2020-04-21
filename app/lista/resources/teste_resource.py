from flask_restful import Resource, reqparse, abort
from flask import request
from datetime import datetime
from lista.models.teste_model import TesteModel
from lista.schemas.teste_schema import TesteSchema
#from lista.schemas.cliente_schema import ClienteSchema

class TesteResource(Resource):
	parser = reqparse.RequestParser()    
	parser.add_argument('empresa',
						type=str,
						required=True,
						help="O nome da empresa não pode estar em branco."
						)
	parser.add_argument('senha',
						type=str,
						required=True,
						help="A senha não pode estar em branco."
						)

	def get(self):
		json = ''
		try:
			return {"message":"try Consegui"},1
		except Exception as e:
			print(e)
			return {"message","except Consegui"},2

		return json,200

	def post(self):
		try:
			data = TesteResource.parser.parse_args()
			#if not data:
			#	return {"message": "Requisição sem JSON"}, 400

			teste = TesteModel(**data)
			teste.adicionar()
			print("teste adicionado")
			testes = TesteModel.listar(0,1)
			schema = TesteSchema(many=True,exclude=['id', 'senha'])
			json = schema.dump(testes)
			return json, 201
			#return {"message": testes}, 400


		except Exception as ex:
			print(ex)
			return {"message": "erro"}, 500

class TestesResource(Resource):
	def get(self):
		json = ""
		try:
			testes = TesteModel.listar(0,1)
			schema = TesteSchema(many=True,exclude=['senha']) 
			json = schema.dump(testes)
		except Exception as e:
			print(e)
			return {"message": "Aconteceu um erro tentando retornar a lista de testes."}, 500
		return json, 200
