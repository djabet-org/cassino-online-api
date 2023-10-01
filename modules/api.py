# This file is part of https://github.com/jainamoswal/Flask-Example.
# Usage covered in <IDC lICENSE>
# Jainam Oswal. <jainam.me>
from .crash_manager import (
    media_velas,
    fetch_contagem_cores,
    get_estrategias,
    fetch_velas
)

from .double_manager import (
    calculate_roll_next_color_probability,
    calculate_rolls_distribution,
    fetch_rolls,
    get_estrategias_double
)

# Import Libraries
from app import app
from flask import jsonify, request
from flask_cors import cross_origin

# from flask_socketio import send, emit
# @socketio.on('opa')
# def handle_json(msg):
#     print('msg: ' + str(msg))


# Define route "/api".
@app.route("/api")
def api():
    # return in JSON format. (For API)
    return jsonify({"message": "Hello from Flask!"})


@app.route("/api/<platform>/crash/dashboard")
@cross_origin()
def dashboard(platform):
    args = request.args
    qtd_velas = args.get("qtdVelas", default=200, type=int)
    qtd_galho = args.get("qtdGalho", default=2, type=int)
    print(qtd_velas)
    print(qtd_galho)

    # return in JSON format. (For API)
    descVelas = fetch_velas(platform, qtd_velas)
    ascVelas = list(reversed(descVelas))

    result = dict()
    result["media_intervalos"] = media_velas(ascVelas)
    result["estrategias"] = get_estrategias(ascVelas, qtd_galho)
    result["contagem_cores"] = fetch_contagem_cores(ascVelas)
    result["velas"] = descVelas
    # result['qtd_velas_total'] = fetch_how_many_velas()
    return jsonify(result)


@app.route("/api/<platform>/double/dashboard/<qtd_velas>")
@cross_origin()
def doubleDashboard(platform, qtd_velas):
    # return in JSON format. (For API)
    descRolls = fetch_rolls(platform, qtd_velas)
    ascRolls = list(reversed(descRolls))

    result = dict()
    result["contagem_cores"] = calculate_rolls_distribution(descRolls)
    result["estrategias"] = get_estrategias_double(ascRolls)
    result["rolls"] = descRolls
    # result['qtd_velas_total'] = fetch_how_many_velas()
    return jsonify(result)

@app.route("/api/blaze/crash/delete/<qtd_velas>", methods=["DELETE"])
def delete(qtd_velas):
    # return in JSON format. (For API)

    velas = fetch_velas(qtd_velas)
    reversedVelas = list(reversed(velas))

    result = dict()
    result["media_intervalos"] = media_velas(reversedVelas)
    result["estrategias"] = get_estrategias(reversedVelas)
    result["contagem_cores"] = fetch_contagem_cores(reversedVelas)
    result["velas"] = velas
    return jsonify(result)
