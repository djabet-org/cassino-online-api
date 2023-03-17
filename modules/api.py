# This file is part of https://github.com/jainamoswal/Flask-Example.
# Usage covered in <IDC lICENSE>
# Jainam Oswal. <jainam.me> 
from .crash_manager import calcular_probabilidades
from .sqlite_helper import fetch_all_crash_points, deletar_velas_antigas

# Import Libraries 
from app import app
from flask import jsonify, request

# Define route "/api".
@app.route('/api')
def api():
  # return in JSON format. (For API)
  return jsonify({"message":"Hello from Flask!"})


@app.route('/api/blaze/crash/probabilidades')
def probabilidades():
  # try:
    max_velas = request.args.get("max_velas", default="1000")
    app.logger.info(max_velas)
    velas = fetch_all_crash_points()

    result = calcular_probabilidades(velas)
    app.logger.info("creu ", result)
    qtd_velas = len(velas)
    result["qtd_velas"] = qtd_velas
    if qtd_velas > 1000:
      deletar_velas_antigas(str(qtd_velas-int(max_velas)))

    # return in JSON format. (For API)
    return jsonify(result)
  # except:
  #   return jsonify("errorrrr")

