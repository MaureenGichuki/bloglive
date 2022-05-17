from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(2000))
    email = db.Column(db.String(2000),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(2000))
    bio = db.Column(db.String(2000))
    profile_pic_path = db.Column(db.String())
    posts=db.relationship('Post',backref = 'user',lazy="dynamic")
    

    
    @property
    def password(self):
        raise AttributeError('Cannot view password')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

   
    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__='roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'Role {self.name}'


class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200))
    post = db.Column(db.String(1000))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    author = db.Column(db.String(240))



    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def delete_post(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_posts(cls,id):
        posts = Post.query.order_by(Post.posted.desc())
        return posts

    def __repr__(self):
        return f'Post {self.post}'

class Comment(db.Model):

    __tablename__='comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(240))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    post_id=db.Column(db.Integer,db.ForeignKey("posts.id"))

 
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
            comments = Comment.query.filter_by(post_id=id).all()
            return comments
    
    def __repr__(self):
        return f'Comment {self.comment}'

class Quote:

    """

    objects for class Quote
    
    """
    def __init__(self,quote, author):
        
        self.quote = quote
        self.author = author
    
    