from datetime import datetime
import os
import os.path
import psycopg2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def fetch_all_crash_points( howMany):

    sqliteConnection = None

    try:
       if os.getenv("FLY_APP_NAME") is None:
            # sqliteConnection = psycopg2.connect(host='localhost', database='postgres', user='aluiz', password='')
            sqliteConnection = psycopg2.connect(host='babar.db.elephantsql.com', database='zzdenalm', user='zzdenalm', password='ZArhVajSHYAd-Pux2dSdovDDaXCO1EZa')

       else:
            sqliteConnection = psycopg2.connect(host='babar.db.elephantsql.com', database='zzdenalm', user='zzdenalm', password='ZArhVajSHYAd-Pux2dSdovDDaXCO1EZa')
        
       cursor = sqliteConnection.cursor()
       sqlite_select_query = "SELECT * FROM crash_points ORDER BY created DESC LIMIT %s;"
       cursor.execute(sqlite_select_query, (howMany,))
       records = list(map(lambda row: row[0], cursor.fetchall()))
       cursor.close()
       return records
    except psycopg2.Error as error:
        print("Failed to fetch crashes", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")  



# def fetch_all_crash_points( howMany, atLeast):

#     sqliteConnection = None

#     try:
#        if os.getenv("FLY_APP_NAME") is None:
#             # sqliteConnection = psycopg2.connect(host='localhost', database='postgres', user='aluiz', password='')
#             sqliteConnection = psycopg2.connect(host='babar.db.elephantsql.com', database='zzdenalm', user='zzdenalm', password='ZArhVajSHYAd-Pux2dSdovDDaXCO1EZa')

#        else:
#             sqliteConnection = psycopg2.connect(host='babar.db.elephantsql.com', database='zzdenalm', user='zzdenalm', password='ZArhVajSHYAd-Pux2dSdovDDaXCO1EZa')
        
#        cursor = sqliteConnection.cursor()
#        sqlite_select_query = "SELECT * FROM crash_points WHERE crash_point >= %s ORDER BY created DESC LIMIT %s);"
#        cursor.execute(sqlite_select_query, (atLeast, howMany,))
#        records = list(map(lambda row: row[0], cursor.fetchall()))
#        cursor.close()
#        return records
#     except psycopg2.Error as error:
#         print("Failed to fetch crashes", error)
#     finally:
#         if sqliteConnection:
#             sqliteConnection.close()
#             # print("The SQLite connection is closed")  

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

