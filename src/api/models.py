from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    name = db.Column(db.String(60), unique=False, nullable=False)
    phone=db.Column(db.String(15),unique=False, nullable =True)

    def __repr__(self):
        return f'<User: {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "phone":self.phone
            # do not serialize the password, its a security breach
        }


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=False, nullable=False)  
    body =  db.Column(db.String(1000), unique=False, nullable=False)
    # ForeinKey y relationship
    use_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable= False)
    user = db.relationship('User')

    def __repr__(self):
        return f'<Post: {self.title}>'

    def serialize(self):
        return { "id": self.id,
                "title": self.title,
                "body": self.body,
                "author": self.user_id
                
         }
    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=False, nullable=False)  
    body =  db.Column(db.String(1000), unique=False, nullable=False)
     # ForeinKey y relationship
    use_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable= False)
    user = db.relationship('User')
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable= False)
    post = db.relationship('Post')
    
    

    def serialize(self):
        return { "id": self.id,
                "title": self.title,
                "body": self.body,
                "author": self.user_id,
                "post": self.post_id
                
         }
    

class Followers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    follower_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    user = db.relationship('User', foreign_keys=[user_id])
    follower = db.relationship('User', foreign_keys=[follower_id])

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "follower_id": self.follower_id
        }

