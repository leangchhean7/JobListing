from flask import Flask,render_template, request,redirect,url_for,flash
from logging import DEBUG
app = Flask(__name__)

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