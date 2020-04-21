from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from lista.models.teste_model import TesteModel

class TesteSchema(ModelSchema):
    class Meta:
        model = TesteModel