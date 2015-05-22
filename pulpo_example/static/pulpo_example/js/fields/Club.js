function ClubField() {

}

ClubField.buildField = function(){
	var field = FieldBase.buildField(this);
	field.field_type = ClubField.name;
	field.options = [];
    field.max_id = 0;
	return (field);
};

// Register field constructor in Factory
fieldFactory.registerField(ClubField.name, ClubField);