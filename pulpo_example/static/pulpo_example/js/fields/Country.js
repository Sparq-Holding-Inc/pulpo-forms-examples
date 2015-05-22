function CountryField() {

}

CountryField.buildField = function(){
	var field = FieldBase.buildField(this);
	field.field_type = CountryField.name;
	field.options = [];
    field.max_id = 0;
	return (field);
};

// Register field constructor in Factory
fieldFactory.registerField(CountryField.name, CountryField);