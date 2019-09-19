from flask import Flask,redirect,url_for,render_template,request,flash


from flask_mail import Mail,Message

from random import randint

from sqlalchemy.orm import sessionmaker

from project_database import Register,Base


from sqlalchemy import create_engine 


engine=create_engine('sqlite:///iii.db')


engine=create_engine('sqlite:///iii.db',connect_args={'check_same_thread':False},echo=True)

Base.metadata.bind=engine

DBsession=sessionmaker(bind=engine)
session=DBsession()


app=Flask(__name__)



app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465

app.config['MAIL_USERNAME']='sandhyasbiiit@gmail.com'

app.config['MAIL_PASSWORD']='9553662247'

app.config['MAIL_USE_TLS']=False

app.config['MAIL_USE_SSL']=True

app.secret_key='abc'

mail=Mail(app)


otp=randint(000000,999999)


@app.route("/email",methods=['POST','GET'])
def email_send():
    return render_template("email.html")
otp=randint(000000,999999)

@app.route("/email_verify",methods=['POST','GET'])
def verify_email():
    email=request.form['email']
    
    msg=Message("One Time Password",sender="sandhyasbiiit@gmail.com",recipients=[email])
    
    msg.body=str(otp)
    
    mail.send(msg)
    
    return render_template("v_email.html")

@app.route("/email_success",methods=['POST','GET'])
def success_email():
    user_otp=request.form['otp']
    if otp==int(user_otp):
        return render_template("email_success.html")
    return "Invalid OTP"

@app.route("/sample")

def demo():
    return "Hello Sandhya Lucky welocome to APSSDC!"

@app.route("/demo_msg")
def d():
    return "<h1>Hello Demo Page</h1>"

@app.route("/info/details")
def s():
    return "<h2>Hello Details</h2>"
@app.route("/details/<name>/<int:age>/<float:salary>")                                                                                   
def info(name,age,salary):
    return "hello {} age {} and salary {}".format(name,age,salary)


@app.route("/admin")
def admin():
    return "hello Admin"

@app.route("/student")
def student():
    return "hello student"


@app.route("/staff")
def staff():
    return "hello staff"


@app.route("/info/<name>")
def admin_info(name):
    if name=='admin':
        return redirect(url_for('admin'))
    elif name=='student':
         return redirect(url_for('student'))
    elif name=='staff':
         return redirect(url_for('staff'))
    else:
        return "No URL"

@app.route("/data/<name>/<int:age>/<float:salary>")
def demo_html(name,age,salary):
    return render_template('sample.html',n=name,a=age,s=salary)


@app.route("/info_data")
def info_data():
    sno=21
    name='sandy'
    branch='IT'
    dept='Trainer'
    return render_template('table_info.html',s_no=sno,n=name,b=branch,d=dept)
    
data=[{'sno':'123','name':'sandy','branch':'IT','dept':'Learner'},{'sno':'13','name':'lucky','branch':'CSE','dept':'Developer'}]
@app.route("/dummy_data")
def dummy():
    return render_template("data.html",dummy_data=data)

@app.route("/table/<int:number>")
def table(number):
    return render_template("table.html",n=number)

@app.route("/file_upload",methods=['GET','POST'])
def file_upload():
    return render_template("file_upload.html")

@app.route("/success",methods=['GET','POST'])
def success():
    if request.method=='POST':
        f=request.files['file']
        f.save(f.filename)
    return render_template("success.html",f_name=f.filename)

@app.route("/show")
def showData():
    register=session.query(Register).all()
    return render_template('show.html',reg=register)

@app.route("/insert",methods=['POST','GET'])
def insertData():
    if request.method=='POST':
        newData=Register(name=request.form['name'],sur_name=request.form['sur_name'],mobile=request.form['mobile'],email=request.form['email'],branch=request.form['branch'],role=request.form['role'])
        session.add(newData)
        session.commit()
        return redirect(url_for('showData'))
    else:
        return render_template("insert.html")


@app.route("/edit/<int:register_id>",methods=['POST','GET'])
def editData(register_id):
    editedData=session.query(Register).filter_by(id=register_id).one()
    if request.method=='POST':
        editedData.name=request.form['name']
        editedData.sur_name=request.form['sur_name']
        editedData.mobile=request.form['mobile']
        editedData.email=request.form['branch']
        editedData.role=request.form['role']


        session.add(editedData)
        session.commit()
        flash("data added...{}".format(editedData.name))


        return redirect(url_for('showData'))
    else:

        return render_template('edit.html',register=editedData)
@app.route("/delete/<int:register_id>",methods=['POST','GET'])
def deleteData(register_id):
    deletedData=session.query(Register).filter_by(id=register_id).one()
    if request.method=='POST':
        session.delete(deletedData)
        session.commit()
        flash("data deleted...")
        return redirect(url_for('showData'))
    else:
        return render_template('delete.html',register=deleteData)



@app.route("/nav_bar")
def nava_bar():
	return render_template('navbar.html',register=editedData)
        
    

if __name__=='__main__':
    app.run(debug=True)