from flask import Flask, render_template,request,redirect, url_for
from classlib import dbImpl,playcardclasses


app = Flask(__name__)

dbtest=dbImpl.dbImpl()

@app.route('/hello/<int:userid>',methods = ['POST', 'GET'])
def hello(userid):
    if(request.method=="POST"):
        try:
            name = request.form['name']
            avatar = request.form['avatar']
            wealth = request.form['wealth']
            player1= playcardclasses.Player(userid,name,wealth,avatar)
            dbtest.updatePlayer(player1)
            msg = "successfully update"
        except:
            msg = "error in insert operation"
        finally:
            return redirect("/")
    else:
        player=dbtest.getPlayerById(userid)
        return render_template('hello.html',userid=userid,player=player)

@app.route('/delete/<int:userid>')
def deleteuser(userid):
     dbtest.deletePlayerById(userid)
     return redirect("/")

@app.route('/create',methods = ['POST', 'GET'])
def createuser():
    if (request.method == "POST"):
        try:
            name = request.form['name']
            avatar = request.form['avatar']
            wealth = request.form['wealth']
            player1 = playcardclasses.Player(0, name, wealth, avatar)
            dbtest.createPlayer(player1)
            msg = "successfully create"
        except:
            msg = "error in insert operation"
        finally:
            return redirect("/")
    else:
        return render_template('newplayer.html')


@app.route('/list')
def list():
    players=dbtest.selectAll()
    return render_template('home.html',players=players)

@app.route('/')
def index():
    return url_for('static', filename='listallplayers.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

