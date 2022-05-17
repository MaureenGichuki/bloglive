from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Email

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write down your bio...',validators = [DataRequired()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    title=StringField('Blog title',validators=[DataRequired()])
    post=TextAreaField('Blog description.',validators = [DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment=TextAreaField('Blog comment.',validators = [DataRequired()])
    submit = SubmitField('Submit')