# This file is part of https://github.com/jainamoswal/Flask-Example.
# Usage covered in <IDC lICENSE>
# Jainam Oswal. <jainam.me> 
from .crash_manager import media_velas, fetch_contagem_cores, get_estrategias, fetch_velas, fetch_how_many_velas

# Import Libraries 
from app import app
from flask import jsonify, request
# from flask_socketio import send, emit
import datetime
import pytz
# @socketio.on('opa')
# def handle_json(msg):
#     print('msg: ' + str(msg))

# Define route "/api".
@app.route('/api')
def api():
  # return in JSON format. (For API)
  return jsonify({"message":"Hello from Flask!"})

@app.route('/api/<platform>/crash/dashboard/<qtd_velas>')
def dashboard(platform, qtd_velas):
  # return in JSON format. (For API)
  velas = fetch_velas(platform, qtd_velas)
  reversedVelas = list(reversed(velas))
  
  result = dict()
  result['media_intervalos'] = media_velas(reversedVelas)
  result['estrategias'] = get_estrategias(reversedVelas)
  result['contagem_cores'] = fetch_contagem_cores(reversedVelas)
  result['velas'] = velas
  result['qtd_velas_total'] = fetch_how_many_velas()
  return jsonify(result)

@app.route('/api/blaze/crash/delete/<qtd_velas>', methods=["DELETE"])
def delete(qtd_velas):
  # return in JSON format. (For API)

  velas = fetch_velas(qtd_velas)
  reversedVelas = list(reversed(velas))
  
  result = dict()
  result['media_intervalos'] = media_velas(reversedVelas)
  result['estrategias'] = get_estrategias(reversedVelas)
  result['contagem_cores'] = fetch_contagem_cores(reversedVelas)
  result['velas'] = velas
  return jsonify(result)

