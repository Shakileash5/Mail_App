from flask import Flask,request,jsonify
from flask_cors import CORS
from crud import *
from mail import *
from otp import *

app = Flask(__name__)
CORS(app)

userDict = {}

@app.route('/register',methods=["GET"])
def register():
    try:
        data = dict(request.args)
        uname = data["uname"]
        mail = data["mail"]
        password = data["password"]
        read_data()
        res = writeData(uname,mail,password)
        print(res)
        if res == -1:
            return jsonify({"result":"Email Already exists"})
        send_mail(mail,uname,0)
        return jsonify({"result":"succesfully"})
    except:
        return jsonify({"result":"400 something went wrong"})

@app.route('/send_otp',methods=["GET"])
def send_otp():
    try:
        data = dict(request.args)
        uname = data["uname"]
        mail = data["mail"]
        password = data["password"]
        read_data()
        #writeData(uname,mail,password)
        otp = generateOTPAlpha(6)
        userDict[otp] = {"uname":uname,"mail":mail,"password":password}
        send_mail(mail,otp,1)
        return jsonify({"result":"succesfully"}) 
    except:
        return jsonify({"result":"400 something went wrong"})

@app.route('/changePassword',methods=["GET"])
def changePassword():
    try:
        data = dict(request.args)
        uname = data["otp"]
        read_data()
        #writeData(uname,mail,password)
        keys = userDict.keys()
        for i in keys:
            if i == uname:
                temp = userDict[i]
                update(temp["uname"],temp['mail'],temp['password'])
        #send_mail(mail,otp,1)
                return jsonify({"result":"succesfully"}) 
        return jsonify({"result":"Unsuccesfully"}) 
    except:
        return jsonify({"result":"400 something went wrong"})

if __name__ == '__main__':
	app.run(debug = True)