from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

from lista.models.fornecedor_model import FornecedorModel

class FornecedorSchema(ModelSchema):
    class Meta:
        model = FornecedorModel