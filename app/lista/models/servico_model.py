from dao import db,Base
from datetime import datetime

class ServicoModel(Base):
	__tablename__ = 'servicos'
	id = db.Column(db.Integer, primary_key=True)
	id_cliente = db.Column(db.String(200), db.ForeignKey('clientes.id'))
	id_fornecedor = db.Column(db.String(200), db.ForeignKey('fornecedores.id'))
	servico = db.Column(db.String(200))
	rank = db.Column(db.Integer)
	contato_fornecedor = db.Column(db.String(200))
	contato_cliente = db.Column(db.String(200))
	data = db.Column(db.DateTime)
	data_criacao = db.Column(db.DateTime)

	def __init__(self, id_cliente, id_fornecedor, servico, contato_fornecedor, contato_cliente, data):
		self.id_cliente = id_cliente
		self.id_fornecedor = id_fornecedor
		self.servico = servico
		self.rank = 0	
		self.contato_fornecedor = contato_fornecedor
		self.contato_cliente = contato_cliente
		self.data = datetime.strptime(data, '%d/%m/%Y')
		self.data_criacao = datetime.now()

	def adicionar(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def modificar(cls, _id, data):
		newItem = cls.query.filter_by(id=_id).first()
		newItem.servico = data['servico']
		newItem.rank = data['rank']
		newItem.contato_fornecedor = data['contato_fornecedor']
		newItem.contato_cliente = data['contato_cliente']
		newItem.data = data['data']
		db.session.commit()
		
	@classmethod
	def encontrar_pelo_id(cls, id):
		return cls.query.filter_by(id=id).first()

	@classmethod
	def listar(cls, _id, _tipo):
		if _tipo == 1:
			return cls.query.all()
		if _tipo == 2:
			return cls.query.filter_by(id_fornecedor=_id)		
		return cls.query.filter_by(id_cliente=_id)

	def remover(self):
		db.session.delete(self)
		db.session.commit()