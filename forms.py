from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField

from wtforms.validators import InputRequired, Email


class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[InputRequired()])
    email = StringField(label='Email', validators=[InputRequired(), Email()])
    subject = StringField(label='Subject', validators=[InputRequired()])
    message = TextAreaField(label='Message', validators=[InputRequired()])
    submit = SubmitField(label='Send message')
