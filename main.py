import json
from flask import Flask, render_template, request, jsonify
from jinja2 import environment
from utils.draw import VigaDraw

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/iBeam', methods=['GET', 'POST',])
def iBeam():
     if request.method == "POST":
        data = json.loads(request.data.decode('utf-8'))
        print( data["h"], data["d"], data["bw"], data["M"])
        image = VigaDraw(data["h"], data["d"], data["bw"], data["M"])
        print(image.CalcArmorDistante(2, 2))
        image.Plot()
        image.DrawViga(True, True)

        circles = [((15, 30), .5), ((5, 20), .5), ((25, 40), .5)]
        image.DrawMultipleArmor(circles)
        image.CalcArmorDistante(4, 12)
        graf = image.CalcArmorDistante(2,2)
        print(graf.show())
        return render_template('iBeam.html')
     else:
        return render_template('iBeam.html')


@app.route('/tBeam', methods=['GET', 'POST',])
def tBeam():
    if request.method == "POST":
        data = json.loads(request.data.decode('utf-8'))
        print( data["h"], data["d"], data["bw"], data["M"])
        image = VigaDraw(data["h"], data["d"], data["bw"], data["M"])
        print(image.CalcArmorDistante(2, 2))
        image.Plot()
        image.DrawViga(True, True)

        circles = [((15, 30), .5), ((5, 20), .5), ((25, 40), .5)]
        image.DrawMultipleArmor(circles)
        image.CalcArmorDistante(4, 12)
        graf = image.CalcArmorDistante(2,2)
        print(graf.show())
        return render_template('tBeam.html')
    else:
        return render_template('tBeam.html')
