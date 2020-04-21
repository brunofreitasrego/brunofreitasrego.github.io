from flask_restful import Resource, reqparse, abort
from flask import request
from datetime import datetime
from lista.models.fornecedor_model import FornecedorModel
#from lista.schemas.schemas import FornecedorSchema
from lista.schemas.fornecedor_schema import FornecedorSchema

class FornecedorResource(Resource):
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
						help="O endereco não pode estar em branco."
						)                                                
	parser.add_argument('ativo',
						type=datetime,
						required=False,
						help="O endereco não pode estar em branco."
						)
	parser.add_argument('servico',
						type=str,
						required=True,
						help="O servico não pode estar em branco."
						)
	parser.add_argument('n_funcionarios',
						type=datetime,
						required=False,
						)                                                
						 
	def get(self,item):
		json = ''
		try:
			usuario = FornecedorModel.encontrar_pelo_id(item)
			print(usuario)
			if usuario:
				schema = FornecedorSchema(exclude=['listas'])
				json = schema.dump(usuario).data
			else:
				return {"message":"Fornecedor de id {} não existe".format(item)},404
		except Exception as e:
			print(e)
			return {"message","Erro na requisição {}".format(item)},500

		return json,200

	def post(self):
		try:
			data = FornecedorResource.parser.parse_args()
			if not data:
				return {"message": "Requisição sem JSON"}, 400

			usuario = FornecedorModel(**data)
			usuario.adicionar()

			user_schema = FornecedorSchema(exclude=['listas'])
			json = user_schema.dump(usuario).data
			return json, 201

		except Exception as ex:
			print(ex)
			return {"message": "erro"}, 500

	def put(self,item):
		json = ""
		try:
			data = FornecedorResource.parser.parse_args()
			if not data:
				return {"message": "Requisição sem JSON"}, 400
			usuario = FornecedorModel.encontrar_pelo_id(item)
			print(usuario)
			if not usuario:
				return {"message": "Usuário não existe"}, 400
			else:
				usuario.modificar(item, data)
				usuario = FornecedorModel.encontrar_pelo_id(item)
				user_schema = FornecedorSchema(exclude=['listas'])
				json = user_schema.dump(usuario).data
				return json, 201

		except Exception as ex:
			print(ex)
			return {"message": "erro"}, 500

	def delete(self, item):
		json = ''
		try:
			usuario = FornecedorModel.encontrar_pelo_id(item)
			print(usuario)
			if usuario:
				usuario.remover() 				
			else:
				return {"message":"Empresa de id {} não existe".format(item)},404
		except Exception as e:
			print(e)
			return {"message","Erro na requisição {}".format(item)},500

		return json,204 

class FornecedoresResource(Resource):
	def get(self):
		json = ""
		try:
			usuarios = FornecedorModel.listar()
			schema = FornecedorSchema(many=True,exclude=['listas'])
			json = schema.dump(usuarios).data
		except Exception as e:
			print(e)
			return {"message": "Aconteceu um erro tentando retornar a lista de fornecedores."}, 500
		return json, 200
