from flask import Flask, render_template, request,jsonify
# from client_info import clientInfo
import client_info
#from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:postgres1234@localhost/height_collector"
          #["SQLALCHEMY_DATABASE_URI"] = Dictionary key
          #postgresql://postgres:postgres1234@localhost/height_collector = Dictionary value
#db=SQLAlchemy(app)

# class Data(db.Model):
#     __table__="data"
#
#     id = db.Column(db.Integer, primary_key=True, nullable=False)
#     email_ = db.Column(db.String(120), unique=True, nullable=False)
#     height_ = db.Column(db.Integer, nullable=False)
#
#     def __init__(self, email_, height_):
#         super(Data, self).__init__()
#         self.email_ = email_
#         self.height_ = height_
# from flask import request
# from flask import jsonify

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.route('/user_ip', methods=['GET'])
def get_tasks():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
    else:
        return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200

@app.route("/") # only "/"= Home page
def index():

    hostInfo = client_info.clientInfo()
    #client_info = [1,2,3,4,5]
    unique_ID = hostInfo[0]
    print(unique_ID)
    mac_ADDRESS = hostInfo[1]
    print(mac_ADDRESS)
    ip_ADDRESS = hostInfo[2]
    print(ip_ADDRESS)

    location_ADDRESS = hostInfo[3]
    print(location_ADDRESS)
    latitude_ADDRESS = hostInfo[3][0]
    print(latitude_ADDRESS)
    longitude_ADDRESS = hostInfo[3][1]
    print(longitude_ADDRESS)

    return render_template("index.html", unique_ID=unique_ID, mac_ADDRESS=mac_ADDRESS, ip_ADDRESS=ip_ADDRESS, location_ADDRESS=location_ADDRESS)

@app.route("/success", methods=["POST"])
def success():
    if request.method=="POST":
        email=request.form["email_name"]
        height=request.form["height_number"]
        #print("Email is : "+email)
        #print("Height is : "+height)
        return render_template("success.html")

if __name__ == "__main__":
    app.debug=True
    app.run() # app.run(port=5001)... Here we can set any port. but default port=5000
