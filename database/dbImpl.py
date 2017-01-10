#!/usr/bin/env python
#-*-encoding:utf-8 -*-
import sqlite3
import playcardclasses
class dbImpl:
    def createPlayer(self,player):
        conn = sqlite3.connect("doudizhu.db")
        c= conn.cursor()
        c.execute("INSERT INTO player VALUES ((SELECT max(id) FROM player)+1, ?, ?, ?)"
        , (player.name,player.wealth,player.avatar))
        conn.commit()
        print "Player inserted successfully"
        conn.close()
    def getPlayerById(self,id):
        conn = sqlite3.connect("doudizhu.db")
        c= conn.cursor()
        c.execute("select * from player where player.id=?"
        , (str(id)))
        # player1=playcardclasses.Player(c.fetchall()[0][0],c.fetchall()[0][1],c.fetchall()[0][2],c.fetchall()[0][3])
        # return player1
        list1=c.fetchall()
        player1=playcardclasses.Player(list1[0][0],list1[0][1],list1[0][2],list1[0][3])
        return player1
        print "Player found successfully"     
    def updatePlayer(self,player):
        conn = sqlite3.connect("doudizhu.db")
        c= conn.cursor()
        c.execute("update player set name=?, wealth=?, avatar=? where id=?"
        , (player.name,player.wealth,player.avatar,player.id))       
        conn.commit()
        conn.close()
        return self.getPlayerById(player.id)
        print "Player updated successfully"
    def deletePlayerById(self,id):
        conn = sqlite3.connect("doudizhu.db")
        c= conn.cursor()
        c.execute("delete from player where id=?"
        , (str(id)) )      
        conn.commit()
        conn.close()
        print "Player deleted successfully"
    def selectAll(self):
        conn = sqlite3.connect("doudizhu.db")
        c= conn.cursor()
        c.execute("select * from player")
        print c.fetchall()
        



        
