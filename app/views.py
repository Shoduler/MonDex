from flask import make_response, request, url_for, jsonify
from app.models import Mon
from app import app, db

def MakePublicMon(mon):
    newMon = {}
    newMon["uri"] = url_for("GetMon", id = mon.id, _external = True)
    newMon["name"] = mon.name
    newMon["desc"] = mon.desc
    newMon["type"] = mon.type
    return newMon

@app.route("/mondex", methods = ["GET"])
def GetAllMon():
    all = Mon.query.all()
    return jsonify({ "mon": [MakePublicMon(m) for m in all] })

@app.route("/mondex/<int:id>", methods = ["GET"])
def GetMon(id):
    try:
        mon = Mon.query.filter(Mon.id == id).one()
        return jsonify({ "mon": MakePublicMon(mon) })
    except:
        return make_response(jsonify({ "ERROR": "NOT FOUND" }), 404)
    return