from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    userId = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.Text)
    email = db.Column(db.Text, unique=True, nullable=False)
    occupation = db.Column(db.Text)
    bio = db.Column(db.Text)
    contact_details = db.Column(db.Text)
    home_address = db.Column(db.Text)
    postal_code = db.Column(db.Text)
    password = db.Column(db.Text, nullable=False)
    images = db.Column(db.Text)


class Post(db.Model):
    __tablename__ = 'Post'
    postId = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.userId'))
    author = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    media = db.Column(db.Text)
    likes = db.Column(db.Integer, default=0)
    comments = db.Column(db.Integer, default=0)
    shares = db.Column(db.Integer, default=0)
    post_date = db.Column(db.Date, default=datetime.utcnow)
    post_time = db.Column(db.Time, default=datetime.utcnow.time)

    # Define foreign key relationship
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

class Comment(db.Model):
    __tablename__ = 'Comment'
    commentId = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.userId'))
    post_id = db.Column(db.Integer, db.ForeignKey('Post.postId'))
    text = db.Column(db.Text)
    post_date = db.Column(db.Date, default=datetime.utcnow)
    post_time = db.Column(db.Time, default=datetime.utcnow.time)

    # Define foreign key relationships
    user = db.relationship('User', backref=db.backref('comments', lazy=True))
    post = db.relationship('Post', backref=db.backref('comments', lazy=True))


class Likes(db.Model):
    __tablename__ = 'Likes'
    likeId = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.userId'))
    post_id = db.Column(db.Integer, db.ForeignKey('Post.postId'))

    # Define foreign key relationships
    user = db.relationship('User', backref=db.backref('likes', lazy=True))
    post = db.relationship('Post', backref=db.backref('likes', lazy=True))


class Shares(db.Model):
    __tablename__ = 'Shares'
    shareId = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.userId'))
    post_id = db.Column(db.Integer, db.ForeignKey('Post.postId'))

    # Define foreign key relationships
    user = db.relationship('User', backref=db.backref('shares', lazy=True))
    post = db.relationship('Post', backref=db.backref('shares', lazy=True))