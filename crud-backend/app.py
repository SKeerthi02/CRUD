from flask import Flask, url_for, render_template, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mysecretpassword@testdb:5432/keerthi'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email, id):
        self.username = username
        self.email = email
        self.id = id

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()
# # keerthi = User(id=1, username='Keerthi', email='keerthi.21094@gmail.com')
# keerthiSuresh = User(id=11, username='keerthiSuresh', email='keerthiSuresh@gmail.com')
# Anamika = User(id=21, username='Anamika', email='Anamika@gmail.com')
# AnkitaKadam = User(id=22, username='AnkitaKadam', email='AnkitaKadam@gmail.com')
# db.session.add(keerthiSuresh)
# db.session.add(Anamika)
#
# db.session.commit()


@app.route('/user', methods=['GET'])
def allUser():
    alluser = User.query.all()
    output = []
    for u in alluser:
        curruser = {}
        curruser['id'] = u.id
        curruser['username'] = u.username
        curruser['email'] = u.email
        output.append(curruser)
    return jsonify(output)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
        if request.method == 'POST':
            name = request.form['name']
            eid = request.form['id']
            email = request.form['email']
            newuser = User(id=eid, username=name, email=email)
            try:
                db.session.add(newuser)
                db.session.commit()
                return redirect('/')
            except:
                return "already exists"

        else:
            return render_template('index.html')


# @app.route("/login", methods=["POST", "GET"])
# def login():
#     return render_template("login.html")
#
#
# @app.route("/<user>")
# def user(usr):
#     return "<h1>{usr}</h1>"


if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
