from flask_wtf import Form
from wtforms import SelectMultipleField, RadioField, IntegerField, FloatField, FieldList, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class SystemSearchForm(Form):
    wh_class = SelectMultipleField("Wormhole Class", choices=[
        ("1", "Class-1"),
        ("2", "Class-2"),
        ("3", "Class-3"),
        ("4", "Class-4"),
        ("5", "Class-5"),
        ("6", "Class-6"),
    ])

    wh_type = RadioField("Wormhole Type", choices=[
        ("1", "All"),
        ("2", "Non-shattered"),
        ("3", "Shattered"),
    ])

    wh_effect = SelectMultipleField("Wormhole Effect", choices=[
        ("1", "No effect"),
        ("2", "Black hole"),
        ("3", "Alpha"),
    ])

    test_boolean1 = BooleanField("Test1")
    test_boolean2 = BooleanField("Test2")

    moon_max = IntegerField("Moon")
    radius = FloatField("Radius")

    authors = FieldList(StringField('Name', [DataRequired()]), min_entries=2, max_entries=4)

    submit = SubmitField("Submit")
