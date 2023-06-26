from datetime import datetime
import os
import os.path
import psycopg2
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

base_url = "https://cassino-database-manager-production.up.railway.app" if os.getenv("ENV") else "http://127.0.0.1:5000"

def fetch_crash_points( howMany):

    response = requests.get(base_url+"/api/cassino/manager/velas/"+ howMany)

    response_json = response.json()
    print(response_json)

    return response_json

# def fetch_crash_points( at_least, startTime, endTime):

#     sqliteConnection = None

#     try:
#        if os.getenv("FLY_APP_NAME") is None:
#             sqliteConnection = psycopg2.connect(host='localhost', database='postgres', user='aluiz', password='')
#        else:
#             sqliteConnection = psycopg2.connect(host='babar.db.elephantsql.com', database='zzdenalm', user='zzdenalm', password='ZArhVajSHYAd-Pux2dSdovDDaXCO1EZa')
        
#        cursor = sqliteConnection.cursor()
#        sqlite_select_query = """SELECT * from crash_points"""
#        cursor.execute(sqlite_select_query)
#        records = list(map(lambda row: row[0], cursor.fetchall()))
#        cursor.close()
#        return records
#     except psycopg2.Error as error:
#         print("Failed to fetch crashes", error)
#     finally:
#         if sqliteConnection:
#             sqliteConnection.close()
#             # print("The SQLite connection is closed")  

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

