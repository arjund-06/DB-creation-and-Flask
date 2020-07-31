from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/login page'
db = SQLAlchemy(app)


class info(db.Model):
    '''
    sno, name ,username, email, age
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    age = db.Column(db.String(12), nullable=False)
    date= db.Column(db.String(12) , nullable=True)



@app.route("/", methods = ['GET', 'POST'])
def login():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        age = request.form.get('age')
        entry = info(name=name, username = username, email= email, age= age, date= datetime.now()) )
        db.session.add(entry)
        db.session.commit()
    return render_template('login.html')


app.run(debug=True)
