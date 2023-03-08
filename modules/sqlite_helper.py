from datetime import datetime
import os.path
import psycopg2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def fetch_all_crash_points():
    try:
        # sqliteConnection = psycopg2.connect(host='babar.db.elephantsql.com', database='zzdenalm', user='zzdenalm', password='ZArhVajSHYAd-Pux2dSdovDDaXCO1EZa')
        sqliteConnection = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='mysecretpassword')
        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")
        sqlite_select_query = """SELECT * from crash_points"""
        cursor.execute(sqlite_select_query)
        records = list(map(lambda row: row[0], cursor.fetchall()))
        print("Quantidade de velas: ", len(records))
        cursor.close()
        return records
    except psycopg2.Error as error:
        print("Failed to fetch crashes", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")            
            
