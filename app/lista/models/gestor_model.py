
from dao import db,Base
from datetime import datetime

class GestorModel(Base):
	__tablename__ = 'usuarios'
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(200))
	senha = db.Column(db.String(200))
	email = db.Column(db.String(200), unique=True)
	tipo = db.Column(db.Integer)
	dataCadastro = db.Column(db.DateTime)

	def __init__(self,nome,senha,email,tipo):
		self.nome = nome
		self.senha = senha
		self.email = email
		self.tipo = tipo
		self.dataCadastro = datetime.now()

	def adicionar(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def modificar(cls, _id, data):
		newItem = cls.query.filter_by(id=_id).first()
		newItem.nome = data['nome']
		newItem.senha = data['senha']
		newItem.email = data['email']
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
