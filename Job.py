from __init__ import db,app

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    category = db.Column(db.String(30))
    description = db.Column(db.Text)
    reqirement = db.Column(db.Text)
    dateLine = db.Column(db.String(50))
    hrName = db.Column(db.String(80))
    hrPhoneNumber = db.Column(db.String(80))
    hrEmail = db.Column(db.String(80))
    hrWebSite = db.Column(db.String(80))
    hrAddress = db.Column(db.Text)

    def __init__(self, title, cat,desc,reqire,dateLine,hrName,hrPhone,hrEmail,hrWeb,hrAddress):
        self.title = title
        self.category = cat
        self.description = desc
        self.reqirement = reqire
        self.dateLine = dateLine
        self.hrName = hrName
        self.hrPhoneNumber = hrPhone
        self.hrEmail = hrEmail
        self.hrWebSite = hrWeb
        self.hrAddress = hrAddress

    @classmethod
    def getAllJobs(self):
        return self.query.all()

    @classmethod
    def getListJobWithCategory(cls,category):
        return cls.query.filter_by(category=category)

    @classmethod
    def getJobByID(cls,selected_id):
        return cls.query.filter_by(id=selected_id).first()


