from flask_restful import Resource, reqparse, abort
from flask import request
from lista.models.gestor_model import GestorModel
from lista.models.fornecedor_model import FornecedorModel
from lista.models.cliente_model import ClienteModel
# from lista.schemas.schemas import Schema
from lista.schemas.gestor_schema import GestorSchema
from lista.schemas.cliente_schema import ClienteSchema
from lista.schemas.fornecedor_schema import FornecedorSchema


class LoginResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="O nome não pode estar em branco."
                        )
    parser.add_argument('senha',
                        type=str,
                        required=True,
                        help="A senha não pode estar em branco."
                        )

    def post(self):
        json = ''
        try:
            data = LoginResource.parser.parse_args()
            usuario = []
            usuario.append(GestorModel.encontrar_pelo_email(data['email']))
            usuario.append(ClienteModel.encontrar_pelo_email(data['email']))
            usuario.append(FornecedorModel.encontrar_pelo_email(data['email']))
            usuario = [i for i in usuario if i is not None][0]
            print(usuario)
            if usuario.tipo == 1 and usuario.senha == data['senha']:
                schema = GestorSchema(exclude=['listas'])
            elif usuario.tipo == 2 and usuario.senha == data['senha']:
                schema = FornecedorSchema(exclude=['listas'])
            elif usuario.tipo == 3 and usuario.senha == data['senha']:
                schema = ClienteSchema(exclude=['listas'])
            else:
                return {"message": "Usuário não existe ou dados incorretos"}, 404
            json = schema.dump(usuario).data
        except Exception as e:
            print(e)
            return {"message", "Erro na requisição"}, 500

        return json, 200

    def get(self, item):
        return '', 200

    def put(self):
        json = ''
        return json, 201
