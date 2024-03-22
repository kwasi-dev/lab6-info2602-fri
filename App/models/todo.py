from App.database import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    text =  db.Column(db.String, nullable=False, unique=True)

    def __init__(self, user_id, text):
        self.user_id = user_id
        self.text = text

    def get_json(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'text': self.text
        }
