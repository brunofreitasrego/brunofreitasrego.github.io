from flask import Flask
from flask_cors import CORS
from flask_restful import Api
# Importar cada recurso usado pela API.
from lista.resources.demanda_resource import DemandaResource, DemandasResource
from lista.resources.servico_resource import ServicoResource, ServicosResource
from lista.resources.login_resource import LoginResource
from lista.resources.cliente_resource import ClienteResource, ClientesResource
from lista.resources.fornecedor_resource import FornecedorResource, FornecedoresResource
from lista.resources.gestor_resource import GestorResource, GestoresResource
from lista.resources.teste_resource import TesteResource, TestesResource

app = Flask(__name__)
# Configurações relativas ao sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

app.secret_key = b'\xc4]gW\x0f\x8d\xc8\x05ocG\xf1\xb1j,{'

# fim configurações relativas ao sqlalchemy
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})  # O uso do cors


# cria as tabelas do banco de dados, caso elas não estejam criadas
@app.before_first_request
def create_tables():
    from dao import db
    db.init_app(app)
    print("criar tabelas")
    db.create_all()


# fim criação de tabelas

api.add_resource(DemandasResource, '/demandas')
api.add_resource(DemandaResource, '/demanda', '/demanda/<int:item>')
api.add_resource(ServicosResource, '/servicos')
api.add_resource(ServicoResource, '/servico', '/servico/<int:item>')

api.add_resource(LoginResource, '/login')
api.add_resource(ClienteResource, '/cliente', '/cliente/<int:item>')
api.add_resource(ClientesResource, '/clientes')
api.add_resource(FornecedorResource, '/fornecedor', '/fornecedor/<int:item>')
api.add_resource(FornecedoresResource, '/fornecedores')
api.add_resource(GestorResource, '/gestor', '/gestor/<int:item>')
api.add_resource(GestoresResource, '/gestores')
api.add_resource(TesteResource, '/teste')
api.add_resource(TestesResource, '/testes')

if __name__ == '__main__':
    from dao import db

    db.init_app(app)
    app.run(port=5000, debug=True)
