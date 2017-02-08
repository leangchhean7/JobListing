from flask import Flask,render_template, request,redirect,url_for,flash
from logging import DEBUG
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)


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
    return render_template('index.html',title="Job Listing Cambodia",jobType=getMenuDic())

@app.route('/job_list')
def jobList():
    return render_template('job_list.html',data=getMenuDic())

@app.route('/details')
def detailsJob():
    return render_template('detail_job.html')
@app.route('/admin_panel')
def adminPanel():
    return render_template('backend/dashboard.html')

@app.route('/admin_panel/add')
def add():
    return render_template('backend/add.html')

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