function PulpoUserField() {

}

PulpoUserField.buildField = function(){
	var field = FieldBase.buildField(this);
	field.field_type = PulpoUserField.name;
	field.options = [];
    field.max_id = 0;
	return (field);
};

// Register field constructor in Factory
fieldFactory.registerField(PulpoUserField.name, PulpoUserField);