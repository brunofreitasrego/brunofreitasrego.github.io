from dao import db,Base
from datetime import datetime

class TesteModel(Base):
	__tablename__ = 'teste'
	id = db.Column(db.Integer, primary_key=True)
	empresa = db.Column(db.String(200))
	senha = db.Column(db.String(200))

	def __init__(self, empresa, senha):
		self.empresa = empresa
		self.senha = senha

	def adicionar(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def modificar(cls, _id, data):
		newItem = cls.query.filter_by(id=_id).first()
		newItem.empresa = data['empresa']
		newItem.senha = data['senha']
		db.session.commit()
		
	@classmethod
	def encontrar_pelo_id(cls, id):
		return cls.query.filter_by(id=id).first()

	@classmethod
	def listar(cls, _id, _tipo):
		if _tipo == 1:
			return cls.query.all()
		if _tipo == 2:
			return cls.query.filter_by(empresa="usp")		
		return cls.query.filter_by(id=id).first()

	def remover(self):
		db.session.delete(self)
		db.session.commit()