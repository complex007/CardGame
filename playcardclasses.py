#!/usr/bin/env python
#-*-encoding:utf-8 -*-
#sfafa
class Card:
    def __init__(self,id,name,image,value):
        self.id=id
        self.name=name
        self.image=image
        self.value=value
    def toDict(self):
        cdict={id:self.id,name:self.name,image:self.image,value:self.value}
        return cdict
class CardBundle:
    def __init__(self,cardList):
        self.cards=cardList
class Player:
    def __init__(self,id,name,image,avatar):
        self.id=id
        self.name=name
        self.image=image
        self.avatar=avatar
class GameRole:
    def __init__(self,player,cardList):
        self.player=player
        self.cards=cardList
    def cardCount(self):
        return len(self.cards)
    def discard(self,cardList):
        self.cards.remove(cardList)
        return cardList
class Farmer(Player):
    def __init__(self):
        Player.__init__(self)
class LandLord(Player):
    def __init__(self):
        Player.__init__(self)
class Dispipe:
    def __init__(self,cards):
        self.cards=cards
    def receive(self,catdBundles):
        self.cards.add(catBundles)
    def cardCount(self):
        return len(self.cards)
class Game:
    def __init__(self,player1,player2,player3):
        self.player1=player1
        self.player2=player2
        self.player3=player3
        self.dispipe=Dispipe()
