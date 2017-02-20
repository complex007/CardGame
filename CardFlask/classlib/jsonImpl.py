
import sqlite3

from classlib import playcardclasses


class jsonImpl:

    def __init__(self):
        self.dname = "classlib/player.json"
    def createPlayer(self,player):
        players=self.selectAll()
        count=len(players)
        player.id=players[count-1]['id']+1
        f = open(self.dname, "a")
        f.write(str(player.toDict())+",")
        f.close()

    def getPlayerById(self,id):
        players=self.selectAll()
        player1=None
        for i in players:
            if i['id']==id :
                player1=playcardclasses.Player(i['id'],i['name'],i['wealth'],i['avatar'])
                break
        return player1

    def updatePlayer(self,player):
        players = self.selectAll()
        for i in players:
            if i['id'] == player.id:
                i['name']=player.name
                i['avatar']=player.avatar
                i['wealth']=player.wealth
                break
        f = open(self.dname, "w")
        for i in players:
            f.write(str(i)+",")
        f.close()


    def deletePlayerById(self,id):
        players = self.selectAll()
        for i in players:
            if i['id'] == id:
                count=players.index(i)
                players.pop(count)
                break
        f = open(self.dname, "w")
        for i in players:
            f.write(str(i)+",")
        f.close()

    def selectAll(self):
        f = open(self.dname, "r")
        content = f.readlines()
        f.close()
        collection = content[0]
        players = eval('[' + collection + ']')
        return players



