# This file is part of https://github.com/jainamoswal/Flask-Example.
# Usage covered in <IDC lICENSE>
# Jainam Oswal. <jainam.me> 
from .crash_manager import media_velas, fetch_contagem_cores, get_estrategias, fetch_velas
from .cassino_database_manager import deletar_velas_antigas

# Import Libraries 
from app import app
from flask import jsonify, request
# from flask_socketio import send, emit

# @socketio.on('opa')
# def handle_json(msg):
#     print('msg: ' + str(msg))

# Define route "/api".
@app.route('/api')
def api():
  # return in JSON format. (For API)
  return jsonify({"message":"Hello from Flask!"})

@app.route('/api/blaze/crash/velas/<qtd_velas>')
def velas(qtd_velas):
  velas = fetch_velas(qtd_velas)
  # send('hey')
  # return in JSON format. (For API)
  return jsonify(velas)

@app.route('/api/blaze/crash/dashboard/<qtd_velas>')
def dashboard(qtd_velas):
  # return in JSON format. (For API)
  result = dict()
  result['media_intervalos'] = media_velas(qtd_velas)
  result['estrategias'] = get_estrategias(qtd_velas)
  result['contagem_cores'] = fetch_contagem_cores(qtd_velas)
  result['velas'] = fetch_velas(qtd_velas)
  return jsonify(result)

@app.route('/api/blaze/crash/media/velas')
def media_intervalos():
    max_velas = request.args.get("max_velas", default="200")
    app.logger.info(max_velas)
    media = media_velas(max_velas)

    app.logger.info("creu ", media)

    # return in JSON format. (For API)
    return jsonify(media)

@app.route('/api/blaze/crash/velas/<qtd>', methods = ['DELETE'])
def delete(qtd):
    deletar_velas_antigas(qtd)

    app.logger.info("deleted!")

    return "deleted!", 204

@app.route('/api/blaze/crash/contagemCores')
def contagemCores():
  # try:
    max_velas = request.args.get("max_velas", default="200")
    app.logger.info(max_velas)
    contagem = fetch_contagem_cores(max_velas)

    app.logger.info("creu ", contagem)

    # return in JSON format. (For API)
    return jsonify(contagem)
  # except:
  #   return jsonify("errorrrr")  

