from dao import db,Base
from datetime import datetime

class ClienteModel(Base):
	__tablename__ = 'clientes'
	id = db.Column(db.Integer, primary_key=True)
	empresa = db.Column(db.String(200), unique=True)
	senha = db.Column(db.String(200))
	email = db.Column(db.String(200), unique=True)
	nome = db.Column(db.String(200))
	endereco = db.Column(db.String(200))
	cnpj = db.Column(db.String(200), unique=True)
	tipo = db.Column(db.Integer)
	ativo = db.Column(db.DateTime)
	dataCadastro = db.Column(db.DateTime)
	listaDemanda = db.relationship("DemandaModel")
	listaServico = db.relationship("ServicoModel")

	def __init__(self, empresa, senha, email, nome, endereco, cnpj, tipo):
		self.nome = nome
		self.empresa = empresa 
		self.senha = senha  
		self.email = email 
		self.nome = nome 
		self.endereco = endereco 
		self.cnpj = cnpj 
		self.tipo = tipo 
		self.ativo = None 
		self.dataCadastro = datetime.now()

	def adicionar(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def modificar(cls, _id, data):
		newItem = cls.query.filter_by(id=_id).first()
		newItem.nome = data['nome']
		newItem.empresa = data['empresa'] 
		newItem.senha = data['senha']  
		newItem.email = data['email'] 
		newItem.nome = data['nome'] 
		newItem.endereco = data['endereco'] 
		newItem.cnpj = data['cnpj'] 
		newItem.tipo = data['tipo']
		db.session.commit()		

	@classmethod
	def encontrar_pelo_id(cls, _id):
		return cls.query.filter_by(id=_id).first()

	@classmethod
	def encontrar_pelo_email(cls, _email):
		return cls.query.filter_by(email=_email).first()

	@classmethod
	def listar(cls):
		return cls.query.all()

	def remover(self):
		db.session.delete(self)
		db.session.commit()
