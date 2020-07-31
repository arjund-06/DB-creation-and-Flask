from flask import Flask,request,render_template,redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/login page'
db = SQLAlchemy(app)

class log(db.Model):
    s_no=db.Column(db.Integer , primary_key=True)
    name= db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email= db.Column(db.String(50), nullable=False)
    age= db.Column(db.Integer , nullable=False)
    date= db.Column(db.String(12) , nullable=True)

@app.route('/', methods=['POST','GET'])
def login():
    if request.method == "POST":
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        age = request.form.get('age')
        # user = log(name = name, username = username, email= email, age= age, date= datetime.now())
        
        db.session.add(log(name = name, username = username, email= email, age= age, date= datetime.now()))
        db.session.commit()
        return render_template('login.html')
    else:
        
        return render_template('login.html')

if __name__==('__main__'):
    app.run(debug=True)