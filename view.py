from __init__ import app,db
from flask import Flask, render_template, request,redirect,url_for
from flask_login import login_required
import flask_login
import flask
from JobCategory import JobCategory
from Job import Job
from User import users,User


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
@login_required
def adminPanel():
    if User.is_active:
        return render_template('backend/dashboard.html')
    else:
        return url_for('login')


@app.route('/admin_panel/list', methods=["GET", "POST"])
@login_required
def list():
    if request.method == "GET":
        list = Job.getAllJobs()

        return render_template(
            'backend/list_job.html',jobs=list
        )
#Operation
@app.route('/admin_panel/delete')
@login_required
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
@login_required
def add():
    if request.method == "GET":

        return render_template('backend/add.html',job_category=JobCategory.getAllJobType())
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
@login_required
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return render_template('backend/login.html')
    email = flask.request.form['email']
    if flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))
    else:
        return redirect(url_for('login',error="wrong password"))
         # return render_template('login.html',error="wrong password")
    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return redirect(url_for('adminPanel'))#'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return render_template('backend/logout.html')
























@app.route('/portfolio')
def portfolio():
    return "Hello is is"















if __name__ == "__main__":
    app.run(debug=True)