from flask import Flask,Response
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

@app.route('/api/player/<int:userid>',methods=["GET", "DELETE"])
def find_player(userid):
    player=dbtest.getPlayerById(userid)
    oneplayer=[player.toDict()]
    return Response(json.dumps(oneplayer))

# @app.route('/api/player/<int:userid>',methods="DELETE")
# def find_player(userid):
#     player=dbtest.deletePlayerById(userid)
#     oneplayer=[player.toDict()]
#     return Response(json.dumps(oneplayer))

if __name__ == '__main__' :
    app.debug = True
    app.run()
