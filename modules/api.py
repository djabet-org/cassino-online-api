# This file is part of https://github.com/jainamoswal/Flask-Example.
# Usage covered in <IDC lICENSE>
# Jainam Oswal. <jainam.me> 
from .crash_manager import calcular_probabilidades, media_velas, fetch_contagem_cores
from .sqlite_helper import fetch_crash_points, deletar_velas_antigas

# Import Libraries 
from app import app
from flask import jsonify, request

# Define route "/api".
@app.route('/api')
def api():
  # return in JSON format. (For API)
  return jsonify({"message":"Hello from Flask!"})

@app.route('/api/blaze/crash/media/velas')
def media_intervalos():
    max_velas = request.args.get("max_velas", default="200")
    app.logger.info(max_velas)
    media = media_velas(max_velas)

    app.logger.info("creu ", media)

    # return in JSON format. (For API)
    return jsonify(media)


@app.route('/api/blaze/crash/probabilidades')
def probabilidades():
  # try:
    max_velas = request.args.get("max_velas", default="200")
    app.logger.info(max_velas)
    velas = fetch_crash_points(max_velas)

    result = calcular_probabilidades(velas)
    app.logger.info("creu ", result)
    qtd_velas = len(velas)
    result["qtd_velas"] = qtd_velas
    # if qtd_velas > 1000:
      # deletar_velas_antigas(str(qtd_velas-int(max_velas)))

    # return in JSON format. (For API)
    return jsonify(result)
  # except:
  #   return jsonify("errorrrr")

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

