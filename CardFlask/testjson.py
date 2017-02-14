from flask import Flask,Response
from flask import request

from classlib import dbImpl,playcardclasses
import json

app = Flask(__name__)
dbtest=dbImpl.dbImpl()

@app.route('/api/player',methods=["GET"])
def list_player():
    players=dbtest.selectAll()
    listplayers=[]
    for item in players:
        player= playcardclasses.Player(item[0],item[1],item[2],item[3])
        listplayers.append(player.toDict())
    return Response(json.dumps(listplayers))

@app.route('/api/player/<int:userid>',methods=["GET"])
def find_player(userid):
    player=dbtest.getPlayerById(userid)
    oneplayer=[player.toDict()]
    return Response(json.dumps(oneplayer))

@app.route('/api/player/<int:userid>',methods=["DELETE"])
def delete_player(userid):
    dbtest.deletePlayerById(userid)

@app.route('/api/player', methods=["POST"])
def add_player():
    name = request.json['name']
    avatar = request.json['avatar']
    wealth = request.json['wealth']
    player1= playcardclasses.Player(0,name,wealth,avatar)
    dbtest.createPlayer(player1)

@app.route('/api/player/<int:userid>', methods=["PUT"])
def update_player(userid):
    player=dbtest.getPlayerById(userid)
    print (player.wealth)
    player.name = request.json['name']
    player.avatar = request.json['avatar']
    player.wealth = request.json['wealth']
    dbtest.updatePlayer(player)



if __name__ == '__main__' :
    app.debug = True
    app.run()
