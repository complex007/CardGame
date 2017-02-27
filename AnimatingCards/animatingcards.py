from flask import Flask,Response
from flask import json
from classlib import cardjsonImpl
from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

dbtest=cardjsonImpl.cardjsonImpl()

@app.route('/views/<path:path>')
def send_file(path):
    return send_from_directory('views', path)

@app.route('/api/card',methods=["GET"])
def show_cards():
    showcards=dbtest.showCards()
    return Response(json.dumps(showcards))




if __name__ == '__main__' :
    app.debug = True
    app.run()