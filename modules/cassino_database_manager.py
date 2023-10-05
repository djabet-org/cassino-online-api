from datetime import datetime
import os
import os.path
import psycopg2
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

base_url = "https://cassino-database-manager-production.up.railway.app"

def fetch_crash_points( platform, howMany):

    response = requests.get("{}/api/{}/crash/{}".format(base_url, platform, howMany))

    response_json = response.json()

    return response_json

def fetch_double_rolls( platform, howMany):

    response = requests.get("{}/api/{}/double/{}".format(base_url, platform, howMany))

    response_json = response.json()

    return response_json

def fetch_how_many_crash_points():
    response = requests.get(base_url+"/api/cassino/manager/velas/howMany")
    response_json = response.json()
    return response_json

def deletar_velas_antigas(qtd):

    sqliteConnection = None

    try:
        if os.getenv("FLY_APP_NAME") is None:
            sqliteConnection = psycopg2.connect(host='localhost', database='postgres', user='aluiz', password='')
        else:
            sqliteConnection = psycopg2.connect(host='babar.db.elephantsql.com', database='zzdenalm', user='zzdenalm', password='ZArhVajSHYAd-Pux2dSdovDDaXCO1EZa')        # sqliteConnection = psycopg2.connect(host='localhost', database='postgres', user='aluiz', password='')
        
        cursor = sqliteConnection.cursor()
        sqlite_select_query = "DELETE FROM crash_points WHERE id IN (SELECT id FROM crash_points ORDER BY created ASC LIMIT %s);"
        cursor.execute(sqlite_select_query, (qtd,))
        sqliteConnection.commit()
        cursor.close()
    except psycopg2.Error as error:
        print("Failed to delete crashes points", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")  

