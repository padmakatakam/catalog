from flask import Flask,redirect,url_for,render_template,request

from flask_Mail import Mail,Message

from random import randint 

app=Flask(__name__)

app.config['MAIL_SERVER']='smtp@gmail.com'

app.config['MAIL_PORT']=465

app.config['MAIL_USERNAME']='sandhyasbiiit@gmail.com'

app.config['MAIL_PASSWORD']='9553662247'

app.config['MAIL_USE_TLS']=false

app.config['MAIL_USE_SSL']=true

mail=Mail(app)


@app.route("/email",methods=['POST','GET'])
def email_send():
    return render_template("email.html")
otp=randint(000000,999999)

@app.route("/email_verify",methods=['POST','GET'])
def verify_email():
    email=request.form['email']
    msg=Message("One Time Password",sender="n151117@rguktn.ac.in",recipients=[email])
    msg.body=str(otp)
    mail.send(msg)
    return render_template("v_email.html")