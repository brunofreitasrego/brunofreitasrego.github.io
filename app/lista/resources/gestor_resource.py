from flask_restful import Resource, reqparse, abort
from flask import request
from lista.models.gestor_model import GestorModel
#from lista.schemas.schemas import GestorSchema
from lista.schemas.gestor_schema import GestorSchema

class GestorResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("nome",
                        type=str,
                        required=True,
                        help="O nome não pode estar em branco."
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
    parser.add_argument('tipo',
                        type=int,
                        required=True,
                        help="O tipo não pode estar em branco."
                        )

    def get(self,item):
        json = ''
        try:
            usuario = GestorModel.encontrar_pelo_id(item)
            print(usuario)
            if usuario:
                schema = GestorSchema(exclude=['listas'])
                json = schema.dump(usuario).data
            else:
                return {"message":"Gestor de id {} não existe".format(item)},404
        except Exception as e:
            print(e)
            return {"message","Erro na requisição {}".format(item)},500

        return json,200

    def post(self):
        try:
            data = GestorResource.parser.parse_args()
            if not data:
                return {"message": "Requisição sem JSON"}, 400

            else:
                usuario = GestorModel(**data)
                usuario.adicionar()
                usuario = GestorModel.encontrar_pelo_email(data['email'])

                user_schema = GestorSchema(exclude=['listas'])
                json = user_schema.dump(usuario).data
                return json, 201

        except Exception as ex:
            print(ex)
            return {"message": "erro"}, 500

    def put(self):
        json = ''
        return json, 201
        
class GestoresResource(Resource):
    def get(self):
        json = ""
        try:
            usuarios = GestorModel.listar()
            schema = GestorSchema(many=True,exclude=['listas'])
            json = schema.dump(usuarios).data
        except Exception as e:
            print(e)
            return {"message": "Aconteceu um erro tentando retornar a lista de gestores."}, 500
        return json, 200
