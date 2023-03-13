from datetime import datetime
import os.path
import psycopg2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def fetch_all_crash_points(max_velas):
    try:
        # sqliteConnection = psycopg2.connect(host='babar.db.elephantsql.com', database='zzdenalm', user='zzdenalm', password='ZArhVajSHYAd-Pux2dSdovDDaXCO1EZa')
        sqliteConnection = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='mysecretpassword')
        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")
        sqlite_select_query = """SELECT * from crash_points ORDER BY created DESC LIMIT %s"""
        cursor.execute(sqlite_select_query, max_velas)
        records = list(map(lambda row: row[0], cursor.fetchall()))
        cursor.close()
        return records
    except psycopg2.Error as error:
        print("Failed to fetch crashes", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")  

def deletar_velas_antigas(qtd):
    try:
        # sqliteConnection = psycopg2.connect(host='babar.db.elephantsql.com', database='zzdenalm', user='zzdenalm', password='ZArhVajSHYAd-Pux2dSdovDDaXCO1EZa')
        sqliteConnection = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='mysecretpassword')
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """DELETE FROM crash_points WHERE id IN (SELECT id FROM crash_points ORDER BY created ASC LIMIT %s);"""
        cursor.execute(sqlite_select_query, qtd)
        cursor.close()
    except psycopg2.Error as error:
        print("Failed to delete crashes points", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")  

