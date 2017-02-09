from flask import Flask,render_template, request,redirect,url_for,flash,session
from logging import DEBUG
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)

import JobType

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

class JobCategory(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(80))
        description = db.Column(db.Text)
        imagepath = db.Column(db.Text)

        def __init__(self,title,desc,imagepath):
            self.title = title
            self.description = desc
            self.imagepath = imagepath


        @classmethod
        def getAllJobType(self):
            return JobCategory.query.all()

def getMenu():
    items = []
    for i in range(1, 10):
        i = str(i)
        items.append(i)
    return items

def getMenuDic():
    itmes = []
    dict = {'title': 'IT Job', 'imageUrl': 'www.google.com' ,'url': 'www.facebook.com', 'desc': 'I love this job'}
    for x in range(9):
        itmes.append(x)
    return (itmes,dict)



#Routing
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html',title="Job Listing Cambodia",jobType=JobCategory.getAllJobType())
@app.route('/job_list/',methods=["GET", "POST"])
def jobList():
    if request.method == "GET":
        data = request.args.get('category_var', None)
        if data == 'all':
            jobs = Job.getAllJobs()
            return render_template('job_list.html',jobs=jobs)
        else:
            jobs = Job.getListJobWithCategory(category=data)

            return render_template('job_list.html',jobs=jobs)

@app.route('/details')
def detailsJob():
    job_id = request.args.get('job_select', None)
    return render_template('detail_job.html',job_selected=Job.getJobByID(job_id))

#backend - admin panel
@app.route('/admin_panel')
def adminPanel():
    return render_template('backend/dashboard.html')

@app.route('/admin_panel/list', methods=["GET", "POST"])
def list():
    if request.method == "GET":
        list = Job.getAllJobs()
        return render_template(
            'backend/list_job.html',jobs=list
        )
#Operation
@app.route('/admin_panel/delete')
def delete():
    try:
        job_id = request.args.get('job_select', None)
        job_to_delete = Job.query.get(job_id)
        db.session.delete(job_to_delete)
        db.session.commit()
        return redirect(url_for('list'))
    except Exception as e:
        return redirect(url_for('list'))



@app.route('/admin_panel/add', methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template('backend/add.html')
    else:
        title = request.form['title']
        cat = request.form['category']
        desc = request.form['description']
        reqire = request.form['reqirement']
        month = request.form['element_4_1']
        day = request.form['element_4_2']
        year = request.form['element_4_3']
        dateLine = day + "/" + month + "/" + year
        hrName = request.form['name']
        hrPhone = request.form['phone']
        hrEmail = request.form['email']
        hrWeb = request.form['website']
        hrAddress = request.form['address']

        job = Job(title=title,cat=cat,desc=desc,reqire=reqire,dateLine=dateLine,hrName=hrName,hrPhone=hrPhone,hrEmail=hrEmail,hrWeb=hrWeb,hrAddress=hrAddress)
        db.session.add(job)
        db.session.commit()
        return redirect("/admin_panel/add")


# @app.route('/admin_panel/add/jobs/create')
# def createJob():
#     return 'create'

@app.route("/admin_login",methods=["GET","POST"])
def adminLogin():

    error = ''
    try:
        if request.method == "POST":
            username = request.form['username']
            password = request.form['password']
            if username == "admin" and password == "123":
                app.logger.debug('user name is ' + username)
                return redirect(url_for('adminPanel'))
            else:
                error = "Invalid Account Password"
                return render_template('backend/login.html', error=error)

        else:
            return render_template('backend/login.html', error="")

    except Exception as e:
            #flash(e)
            error = 'invalid Account'
            return render_template('backend/login.html', error=error)





@app.route('/portfolio')
def portfolio():
    return "Hello is is"

if __name__ == "__main__":
    app.run(debug=True)