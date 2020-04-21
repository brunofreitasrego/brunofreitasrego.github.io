from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from lista.models.demanda_model import DemandaModel

class DemandaSchema(ModelSchema):
    listaDemanda = fields.Nested("DemandaModel", many=True, exclude=('itens','usuario'))
    class Meta:
        model = DemandaModel