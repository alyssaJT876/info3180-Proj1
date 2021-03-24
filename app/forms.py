from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired, Email

class PropertyForm(FlaskForm):
	title = StringField('Title', validators=[InputRequired()])
	description = TextAreaField('Description', validators=[InputRequired()])
	bed = StringField('Bedrooms', validators=[InputRequired()])
	bath = StringField('Bathrooms', validators=[InputRequired()])
	price = StringField('Price', validators=[InputRequired()])
	propType = SelectField("Type", choices=[('House', 'House'), ('Apartment', 'Apartment')])
	location = StringField('Location', validators=[InputRequired()])
	picture = FileField('Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])