from __init__ import app,db


class JobCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    imagepath = db.Column(db.Text)

    def __init__(self, title, desc, imagepath):
        self.title = title
        self.description = desc
        self.imagepath = imagepath


    @classmethod
    def getAllJobType(self):
        return JobCategory.query.all()