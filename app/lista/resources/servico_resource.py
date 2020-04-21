from flask_restful import Resource, reqparse, abort
from flask import request
from lista.models.servico_model import ServicoModel
from lista.schemas.servico_schema import ServicoSchema

class ServicoResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('id_cliente',
						type=int,
						required=True,
						help="O id do cliente não pode estar em branco."
						)
	parser.add_argument('id_fornecedor',
						type=int,
						required=True,
						help="O id do fornecedor não pode estar em branco."
						)
	parser.add_argument('servico',
						type=str,
						required=True,
						help="O serviço não pode estar em branco."
						)                                                    
	parser.add_argument('contato_fornecedor',
						type=str,
						required=True,
						help="O contato_fornecedor não pode estar em branco."
						)
	parser.add_argument('contato_cliente',
						type=str,
						required=True,
						help="O contato_cliente não pode estar em branco."
						)
	parser.add_argument('data',
						type=str,
						required=True,
						help="A data não pode estar em branco."
						)

	def get(self, item):
		json = ''
		try:
			item = ServicoModel.encontrar_pelo_id(item)
			if item:
				schema = ServicoSchema(exclude=['listas'])
				json = schema.dump(item).data
			else:
				abort(404, message="Item {} não está na lista".format(item))
		except Exception as e:
			print(e)
			abort(404, message="Item {} não está na lista".format(item))

		return json,201

	def post(self):
		json = ''
		try:
			data = ServicoResource.parser.parse_args()
			item = ServicoModel(**data)
			item.adicionar()
			schema = ServicoSchema(exclude=['listas'])
			json = schema.dump(item).data
		except Exception as e:
			print(e)
			abort(500, message="Erro no POST")
		return json, 201

	def delete(self, item):
		json = []
		try:
			item = ServicoModel.encontrar_pelo_id(item)
			if item:
				item.remover()
				lista = ServicoModel.listar(0, 1)
				schema = ServicoSchema(many=True,exclude=['listas'])
				json = schema.dump(lista).data
			else:
				return {"message":"Item {} não está na lista".format(item)},404
		except Exception as e:
			print(e)
		return json, 201

	def put(self,item):
		json = ""
		try:
			data = ServicoResource.parser.parse_args()
			if not data:
				return {"message": "Requisição sem JSON"}, 400
			servico = ServicoModel.encontrar_pelo_id(item)
			print(servico)
			if not servico:
				return {"message": "Serviço não existe"}, 400
			else:
				servico.modificar(item, data)
				servico = ServicoModel.encontrar_pelo_id(item)
				servico_schema = ServicoSchema(exclude=['listas'])
				json = servico_schema.dump(servico).data
				return json, 201

		except Exception as ex:
			print(ex)
			return {"message": "erro"}, 500

class ServicosResource(Resource):
	def get(self):
		json = []
		args = request.args
		try:
			if "id" in args and "tipo" in args: 
				idUsuario, tipo = 0, 0
				idUsuario, tipo = args['id'], args['tipo']
				itens = ServicoModel.listar(idUsuario, tipo)
			else:
				itens = ServicoModel.listar(0, 1)
			
			schema = ServicoSchema(many=True,exclude=['listas'])
			json = schema.dump(itens).data
		except Exception as e:
			print(e)
			return {"message": "Aconteceu um erro tentando retornar a lista de servicos."}, 500
		return json,201