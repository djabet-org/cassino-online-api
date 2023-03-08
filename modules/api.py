# This file is part of https://github.com/jainamoswal/Flask-Example.
# Usage covered in <IDC lICENSE>
# Jainam Oswal. <jainam.me> 
from .crash_manager import calcular_probabilidades
from .sqlite_helper import fetch_all_crash_points

# Import Libraries 
from app import app
from flask import jsonify

# Define route "/api".
@app.route('/api')
def api():
  # return in JSON format. (For API)
  return jsonify({"message":"Hello from Flask!"})


@app.route('/api/blaze/crash/probabilidades')
def probabilidades():
  velas = fetch_all_crash_points()
  result = calcular_probabilidades(velas)
  result["qtd_velas"] = len(velas)

  # return in JSON format. (For API)
  return jsonify(result)  
