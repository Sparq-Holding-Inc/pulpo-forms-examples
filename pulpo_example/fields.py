from pulpo_forms.fieldtypes import ModelField
from pulpo_forms.fieldtypes import FieldFactory
from .models import PulpoUser, Club, Country


class PulpoUserField(ModelField.ModelField):
    prp_template_name = "usuario/properties.html"
    model = PulpoUser
    name = "PulpoUser"

    def get_assets():
        return ['pulpo_example/js/fields/PulpoUser.js']

    def __str__(self):
        return "PulpoUser"

FieldFactory.FieldFactory.register('PulpoUserField', PulpoUserField)


class CountryField(ModelField.ModelField):
    prp_template_name = "club/properties.html"
    model = Country
    name = "Country"

    def get_assets():
        return ['pulpo_example/js/fields/Country.js']

    def __str__(self):
        return "Country"

FieldFactory.FieldFactory.register('CountryField', CountryField)


class ClubField(ModelField.ModelField):
    prp_template_name = "club/properties.html"
    model = Club
    name = "Club"

    def get_assets():
        return ['pulpo_example/js/fields/Club.js']

    def __str__(self):
        return "Club"

FieldFactory.FieldFactory.register('ClubField', ClubField)
