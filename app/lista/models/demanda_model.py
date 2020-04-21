from dao import db,Base
from datetime import datetime

class DemandaModel(Base):
	__tablename__ = 'demandas'
	id = db.Column(db.Integer, primary_key=True)
	cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"))
	status = db.Column(db.String(200))
	custo = db.Column(db.String(200))
	problema = db.Column(db.String(10000))
	solucao = db.Column(db.String(10000))
	data_criacao = db.Column(db.DateTime)

	def __init__(self, cliente_id, status, custo, problema, solucao):
		self.status = status
		self.cliente_id = cliente_id
		self.custo = custo
		self.problema = problema
		self.solucao = solucao
		self.data_criacao = datetime.now()

	def adicionar(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def modificar(cls, _id, data):
		newItem = cls.query.filter_by(id=_id).first()
		newItem.status = data['status']
		newItem.custo = data['custo']
		newItem.problema = data['problema']
		newItem.solucao = data['solucao']
		db.session.commit()

	@classmethod
	def encontrar_pelo_id(cls, _id):
		return cls.query.filter_by(id=_id).first()

	@classmethod
	def encontrar_pelo_email(cls, _email):
		return cls.query.filter_by(email=_email).first()

	@classmethod
	def listar(cls, _id):
		if _id == 1:
			return cls.query.all()
		return cls.query.filter_by(cliente_id = _id)

	def remover(self):
		db.session.delete(self)
		db.session.commit()