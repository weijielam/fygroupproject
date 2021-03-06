# app/user/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange, InputRequired

list_choices = [('Donation', 'Donation'), ('Pledge', 'Pledge')]

class paymentForm(FlaskForm):
	dol_amount = IntegerField('Euro', validators=[InputRequired()])
	cent_amount = IntegerField('Cents', validators=[InputRequired(), NumberRange(min=0, max=99, message="please enter a number between 0 and 99")])
	pay_type = SelectField('Type', choices = list_choices, validators=[DataRequired()])
	purpose = SelectField('Purpose', coerce=int)
	submit = SubmitField('Submit')