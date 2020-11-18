
import sqlite3
import os
import datetime
import smtplib
from flask import Flask, render_template, url_for, request, jsonify


app = Flask(__name__)

#Data Models
basedir=os.path.join(os.path.abspath(os.path.dirname(__file__)), "db.sqlite")


@app.route('/')
def index():
    return render_template('index.htm')


@app.route('/register', methods=['POST'])
def register():
	user = request.get_json()
	#Database
	connection=sqlite3.connect(basedir, detect_types=sqlite3.PARSE_DECLTYPES)
	connection.row_factory = sqlite3.Row
	cursor=connection.cursor()
	try:
		cursor.execute("CREATE TABLE user(id INTEGER PRIMARY KEY AUTOINCREMENT, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, user_fname TEXT, user_lname TEXT, user_email TEXT, user_phone TEXT)")
	except:
		pass
	timestamp=str(datetime.datetime.now())
	first_name=user['first_name']
	second_name=user['last_name']
	email=user['email']
	phone=user['phone']
	cursor.execute("INSERT INTO user(created,user_fname,user_lname,user_email,user_phone) VALUES(?,?,?,?,?)", (timestamp,first_name,second_name,email,phone))
	connection.commit()
	connection.close()
	#Email
	#smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	#smtpObj.ehlo()
	#smtpObj.starttls()
	#smtpObj.login('chachaian1997@gmail.com', 'kehancha1997')
	#smtpObj.sendmail('chachaian1997@gmail.com', email, f'Subject: Hello {first_name} .\nWelcome at Webicians')
	#smtpObj.quit()
	return {"user_name":first_name, "message":"Your information has been received. We will send you an email in a few seconds. Kindly check your email for more information."}

if __name__=='__main__':
	app.run(debug=True)