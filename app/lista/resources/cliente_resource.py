from flask_restful import Resource, reqparse, abort
from flask import request
from datetime import datetime
from lista.models.cliente_model import ClienteModel
#from lista.schemas.schemas import ClienteSchema
from lista.schemas.cliente_schema import ClienteSchema

class ClienteResource(Resource):
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
	parser.add_argument('email',
						type=str,
						required=True,
						help="O email não pode estar em branco."
						)                                                    
	parser.add_argument("nome",
						type=str,
						required=True,
						help="O nome não pode estar em branco."
						)
	parser.add_argument('endereco',
						type=str,
						required=False,
						)
	parser.add_argument('cnpj',
						type=str,
						required=True,
						help="O cnpj não pode estar em branco."
						)
	parser.add_argument('tipo',
						type=int,
						required=True,
						help="O tipo não pode estar em branco."
						)

	def get(self,item):
		json = ''
		try:
			usuario = ClienteModel.encontrar_pelo_id(item)
			print(usuario)
			if usuario:
				schema = ClienteSchema(exclude=['listas'])
				json = schema.dump(usuario).data
			else:
				return {"message":"Empresa de id {} não existe".format(item)},404
		except Exception as e:
			print(e)
			return {"message","Erro na requisição {}".format(item)},500

		return json,200

	def post(self):
		try:
			data = ClienteResource.parser.parse_args()
			if not data:
				return {"message": "Requisição sem JSON"}, 400

			usuario = ClienteModel(**data)
			usuario.adicionar()
			schema = ClienteSchema(exclude=['listas'])
			json = schema.dump(usuario).data
			return json, 201

		except Exception as ex:
			print(ex)
			return {"message": "erro"}, 500

	def put(self,item):
		json = ""
		try:
			data = ClienteResource.parser.parse_args()
			if not data:
				return {"message": "Requisição sem JSON"}, 400
			usuario = ClienteModel.encontrar_pelo_id(item)
			print(usuario)
			if not usuario:
				return {"message": "Usuário não existe"}, 400
			else:
				usuario.modificar(item, data)
				schema = ClienteSchema(exclude=['listas'])
				json = schema.dump(usuario).data
				return json, 201

		except Exception as ex:
			print(ex)
			return {"message": "erro"}, 500

	def delete(self, item):
		json = ''
		try:
			usuario = ClienteModel.encontrar_pelo_id(item)
			print(usuario)
			if usuario:
				usuario.remover() 				
			else:
				return {"message":"Empresa de id {} não existe".format(item)},404
		except Exception as e:
			print(e)
			return {"message","Erro na requisição {}".format(item)},500

		return json,204 

class ClientesResource(Resource):
	def get(self):
		json = ""
		try:
			usuarios = ClienteModel.listar()
			schema = ClienteSchema(many=True,exclude=['listas'])
			json = schema.dump(usuarios).data
		except Exception as e:
			print(e)
			return {"message": "Aconteceu um erro tentando retornar a lista de clientes."}, 500
		return json, 200
