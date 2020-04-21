from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from lista.models.servico_model import ServicoModel

class ServicoSchema(ModelSchema):
    listas = fields.Nested("ServicoModel", many=True)
    class Meta:
        model = ServicoModel