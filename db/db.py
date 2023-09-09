###############################
### MCCT                    ###
###############################

import traceback
import mysql.connector
import os

from dotenv import load_dotenv
from db import connect

ENV = os.getenv("ENV")
PROJECT_DIR = os.getenv("PROJECT_DIR")

DB_CONFIG = {
    "user": connect.dbuser,
    "password": connect.dbpass,
    "host": connect.dbhost,
    "port": connect.dbport,
    "database": connect.dbname,
    "auth_plugin": "mysql_native_password",
}

##################################################


def sql_exec_with_file(path):
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    try:
        with open(path, "r") as sql_file:
            re_create_schema = (
                f"DROP SCHEMA IF EXISTS {connect.dbname};"
                f"CREATE SCHEMA {connect.dbname};"
                f"USE {connect.dbname};"
            )
            splited_sql = (re_create_schema + sql_file.read()).split("COMMIT;")
            for sql in splited_sql:
                result_iterator = cursor.execute(f"{sql}\nCOMMIT;", multi=True)
                for res in result_iterator:
                    debug_print_result(f"{res.statement}", icon="⬆️ ")
                    debug_print_result(f"Affected {res.rowcount} rows")
                connection.commit()
    except BaseException as e:
        debug_print_result(str(e), icon="🚨")
        connection.rollback()
        traceback.print_exc()
    finally:
        cursor.close()
        connection.close()


def sql_exec_with_connection(query, params=None, callback=None):
    connection = mysql.connector.connect(**DB_CONFIG)

    if not connection or not connection.is_connected():
        raise mysql.connector.Error("connot connect to database")

    cursor = connection.cursor()

    try:
        result = None

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        debug_print_result(f"{cursor.statement}", icon="⬆️ ")

        if callback:
            result = callback(cursor)

        connection.commit()
        return result
    except mysql.connector.Error as e:
        debug_print_result(f"{e.msg}", icon="🚨")
        debug_print_result(f"{cursor.statement}", icon="⬆️ ")
        connection.rollback()
        traceback.print_exc()
        return False
    finally:
        cursor.close()
        connection.close()


def sql_exec(query, params=None, callback=None):
    return sql_exec_with_connection(query, params=params, callback=callback)


##################################################


# output: `[{"name": ""}, {"title2": ""},]`
def get_mapped_titles_rows(cursor, print=True):
    rows = cursor.fetchall()

    titles = []
    if cursor.description != None:
        titles = [desc[0] for desc in cursor.description]

    if len(rows) == 0:
        rows = []

    output = [
        {titles[i]: rows[j][i] for i in range(len(titles))} for j in range(len(rows))
    ]

    if print:
        debug_print_result(output, icon="⬇️ ")

    return output


# output: `{"name": ""}`
def get_first_mapped_title_row(cursor):
    output = get_mapped_titles_rows(cursor, False)
    if len(output) == 0:
        output = {}
    else:
        output = output[0]
    debug_print_result(output, icon="⬇️ ")
    return output


##################################################


def get_rows(cursor):
    rows = cursor.fetchall()

    if len(rows) == 0:
        rows = []

    output = {}
    output.update({"rows": rows})

    debug_print_result(output, icon="⬇️ ")

    return output


# output:
# {titles: ["name", ""], rows: [("aaa", ""), ("bbb", ""]}
def get_titles_rows(cursor):
    rows = cursor.fetchall()

    titles = []
    if cursor.description != None:
        titles = [desc[0] for desc in cursor.description]

    if len(rows) == 0:
        rows = []

    output = {}
    output.update({"titles": titles})
    output.update({"rows": rows})

    debug_print_result(output, icon="⬇️ ")

    return output


##################################################


def get_lastrowid(cursor):
    lastrowid = cursor.lastrowid
    debug_print_result(lastrowid, icon="⬇️ ")
    return lastrowid


##################################################


def debug_print_result(result, icon="▶️"):
    if ENV == "DEVELOPMENT":
        if type(result) == list:
            for line in result:
                print(f"{icon}", end="")
                if type(line) == dict:
                    for k, v in line.items():
                        print(f"\t{k:>12}: {v}")
                else:
                    print(f"{icon} {line}")
        elif type(result) == dict:
            print(f"{icon}", end="")
            for k, v in result.items():
                print(f"\t{k:>12}: {v}")
        else:
            print(f"{icon} {result}")


##################################################

if __name__ == "__main__":
    db_result = sql_exec("Show tables;", callback=get_rows)
    print(db_result)
