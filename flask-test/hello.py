from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/potato/')
def potato():
    return 'i want some potatoes'

@app.route('/user/<username>/')
def getUserName(username):
    return 'username %s' % username

@app.route("/integers/<int:id_user>/")
def getIdUser(id_user):
    return 'this page only receives integers, integer: %d' % id_user