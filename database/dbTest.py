#!/usr/bin/env python
#-*-encoding:utf-8 -*-
import dbImpl
import playcardclasses
dbtest=dbImpl.dbImpl()
# player1=playcardclasses.Player(1,"test3",2,"test.jpg")
# dbtest.createPlayer(player1)
# dbtest.selectAll()
# player2= dbtest.getPlayerById(3)
# print player2.avatar
# print dbtest.updatePlayer(player1).name
# dbtest.deletePlayerById(1)
dbtest.selectAll()