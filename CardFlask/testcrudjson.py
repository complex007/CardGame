from classlib import jsonImpl,playcardclasses
import json

# f=open("classlib/player.json","r")
#
# # f.write(', {"wealth": 3, "id": 8, "avatar": "test3.jpg", "name": "test3"}')
# content=f.readlines()
# f.close()
# collection=content[0]
# players = eval('[' + collection + ']')
#
# print(players)
#
# players.pop(0)
# print(players[0]['id'])


jsontest=jsonImpl.jsonImpl()

print(jsontest.selectAll())

jsonplayer=jsontest.getPlayerById(9)

print(jsonplayer.toDict())

player1=playcardclasses.Player(9,"test9",3,"test9.jpg")

# jsontest.createPlayer(player1)
# jsontest.updatePlayer(player1)
jsontest.deletePlayerById(9)
# jsonplayer2=jsontest.getPlayerById(9)
# print(jsonplayer2.toDict())

print(jsontest.selectAll())



