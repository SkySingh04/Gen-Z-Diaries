from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL,Email

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterUserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

class LoginUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class DeleteForm(FlaskForm):
    email = StringField("Type 'OK' To Delete", validators=[DataRequired()])
    submit = SubmitField("Delete")

class CommentsForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Upload Comment")
