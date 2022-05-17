from curses import flash
from flask import render_template,redirect,url_for,abort

from app.requests import get_quote
from . import main
from flask_login import login_required,current_user
from ..models import User,Comment,Post
from .forms import UpdateProfile,CommentForm,PostForm

from .. import db


@main.route('/')
def index():
    '''
    root page function that returns the index page

    '''

    quote = get_quote()

    return render_template('index.html', quote=quote)

@main.route('/allblogs')
def allblogs():

    posts=Post.get_posts(id)
    return render_template('allblogs.html',posts=posts)



@main.route('/new/post',methods= ['GET','POST'])
@login_required
def newpost():

    form=PostForm()

    if form.validate_on_submit():
        title = form.title.data
        post=form.post.data
        new_post=Post(title=title,post=post,user=current_user)
        new_post.save_post()
        return redirect(url_for('main.allblogs'))

    return render_template('post.html',post_form=form)


@main.route('/post/comment',methods= ['GET','POST'])
@login_required
def post_comment():

    form = CommentForm()

    comments = Comment.query.all()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment=comment)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.allblogs'))


    return render_template('comment.html',comment_form=form,comment=comments)

@main.route('/delete/comment',methods= ['GET','POST'])
@login_required
def delete_comment(id):


    comments = Comment.query.filter_by(id=id).first()

    Comment.delete_comment(id)
   
    return redirect(url_for('main.allblogs'))




@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

