from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class BooksForm(FlaskForm):
    author = StringField("Author", validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired()])
    genre = StringField("Genre")
    available = BooleanField("Available")