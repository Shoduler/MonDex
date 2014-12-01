from app import db

class Mon(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(16))
    desc = db.Column(db.String(256))
    type = db.Column(db.String(8))

    def __repr__(self):
        return ("<Mon #{1}: {2}".format(self.id, self.title))