from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from lista.models.gestor_model import GestorModel
class GestorSchema(ModelSchema):
    class Meta:
        model = GestorModel