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
  max_velas = request.args.get("max_velas",default="1000")
  velas = fetch_all_crash_points(max_velas)
  app.logger.info("Quantidade de velas: ", len(max_velas))

  result = calcular_probabilidades(velas)
  qtd_velas = len(velas)
  result["qtd_velas"] = qtd_velas
  if qtd_velas > 1000:
    deletar_velas_antigas(qtd_velas-1000)
    

  # return in JSON format. (For API)
  return jsonify(result)  
