
from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3
from ultralytics import YOLO
import cv2
from datetime import datetime


app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load YOLO model
model = YOLO('best.pt')

# @app.route('/detect', methods=['POST'])
# def detect():
#     if 'file' not in request.files:
#         return 'No file part'

#     file = request.files['file']
#     if file.filename == '':
#         return 'No selected file'

#     if file:
#         # Save uploaded image
#         filename = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + file.filename
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)

#         # Run detection
#         results = model(filepath)

#         # Save result image (annotated)
#         result_img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result_' + filename)
#         result_image = results[0].plot()
#         cv2.imwrite(result_img_path, result_image)

#         # Send image to result.html
#         img_src = '/' + result_img_path  # relative URL for HTML
#         return render_template("result.html", img_src=img_src)

#     return redirect(url_for('index'))
@app.route('/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        # Save uploaded image
        filename = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Run detection
        results = model(filepath)

        # Check if any tumor was detected
        detections = results[0].boxes  # For YOLOv8 or YOLOv5 models
        if len(detections) == 0:
            # No tumor detected → invalid image
            message = "Invalid image! No brain tumor detected."
            return render_template("result.html", img_src=None, message=message)

        # If detected → save and display the annotated result
        result_img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result_' + filename)
        result_image = results[0].plot()
        cv2.imwrite(result_img_path, result_image)

        img_src = '/' + result_img_path
        return render_template("result.html", img_src=img_src, message=None)

    return redirect(url_for('index'))


@app.route("/signup")
def signup():
    global otp, username, name, email, number, password
    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
    con.commit()
    con.close()
    return render_template("signin.html")

@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("index.html")
    else:
        return render_template("signin.html")

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/index')
def index():
	return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')

   
if __name__ == '__main__':
    app.run(debug=False)