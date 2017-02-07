from flask import Flask,render_template
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

@app.route("/admin_login")
def adminLogin():
    return render_template('backend/login.html')

@app.route('/portfolio')
def portfolio():
    return "Hello is is"

if __name__ == "__main__":
    app.run(debug=True)