
class cardjsonImpl:

    def __init__(self):
        self.dname = "classlib/cards.json"

    def showCards(self):
        f = open(self.dname, "r")
        content = f.readlines()
        f.close()
        collection = content[0]
        cards = eval(collection)
        return cards