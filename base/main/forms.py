from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired


class TakeImageForm(FlaskForm):
    image = FileField('Picture', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')
