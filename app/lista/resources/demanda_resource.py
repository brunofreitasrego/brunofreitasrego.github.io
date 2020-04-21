from flask_restful import Resource, reqparse, abort
from flask import request
from lista.models.demanda_model import DemandaModel
from lista.schemas.demanda_schema import DemandaSchema

class DemandaResource(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('status',
						type=str,
						required=True,
						help="O status não pode estar em branco."
						)
	parser.add_argument('custo',
						type=str,
						required=False,
						)
	parser.add_argument('problema',
						type=str,
						required=True,
						help="O problema não pode estar em branco."
						)                                                    
	parser.add_argument("solucao",
						type=str,
						required=False
						)
	parser.add_argument('cliente_id',
						type=str,
						required=False,
						)

	def get(self,item):
		json = ''
		try:
			item = DemandaModel.encontrar_pelo_id(item)
			if item:
				schema = DemandaSchema(exclude=['listas'])
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
			data = DemandaResource.parser.parse_args()
			item = DemandaModel(**data)
			item.adicionar()
			schema = DemandaSchema(exclude=['listas'])
			json = schema.dump(item).data
		except Exception as e:
			print(e)
			abort(500, message="Erro no POST")
		return json, 201

	def delete(self, item):
		json = ''
		try:
			demanda = DemandaModel.encontrar_pelo_id(item)
			print(demanda)
			if demanda:
				demanda.remover() 				
			else:
				return {"message":"Demanda de id {} não existe".format(item)},404
		except Exception as e:
			print(e)
			return {"message","Erro na requisição {}".format(item)},500

		return json,204 

	def put(self,item):
		json = ''
		try:
			data = DemandaResource.parser.parse_args()
			if not data:
				return {"message": "Requisição sem JSON"}, 400
			demanda = DemandaModel.encontrar_pelo_id(item)
			print(demanda)
			if not demanda:
				return {"message": "Usuário não existe"}, 400
			else:
				demanda.modificar(item, data)
				demanda = DemandaModel.encontrar_pelo_id(item)
				demanda_schema = DemandaSchema(exclude=['listas'])
				json = demanda_schema.dump(demanda).data
				return json, 201

		except Exception as ex:
			print(ex)
			return {"message": "erro"}, 500

class DemandasResource(Resource):
	def get(self):
		json = []
		args = request.args
		try:
			idCliente = 0
			if "id" in args:
				idCliente = args['id']
				itens = DemandaModel.listar(idCliente) 
			else:
				itens = DemandaModel.listar(1)
			schema = DemandaSchema(many=True, exclude=['listas'])
			json = schema.dump(itens).data
		except Exception as e:
			print(e)
			return {"message": "Aconteceu um erro tentando retornar a lista de demandas."}, 500
		return json,201