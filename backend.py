import psycopg2
from psycopg2.sql import SQL, Identifier
from time import time

DBNAME = "DB_Lab1"
USERNAME = "postgres"
DBPASSWORD = "12345"

def insert_one(cursor, table_name, list):

    if table_name == "employeers":
        cursor.execute("""INSERT INTO "employeers" ("name", "phone_number", "position",  "salary" ,"department_id") VALUES(%s, %s, %s, %s, %s)""",(list[0], list[1], list[2], list[3], list[4]))

    elif table_name == "kitchen_department":
        cursor.execute("""INSERT INTO "kitchen_department" ("name_of_department", "employeers_count", "certificate_id", "book_id") VALUES (%s, %s, %s, %s)""",(list[0], list[1], list[2], list[3]))

    elif table_name == "quality_certificate":
        cursor.execute("""INSERT INTO "quality_certificate" ("date_of_issue","expirition_date","authority_that_issued") VALUES (%s, %s, %s)""",(list[0], list[1], list[2]))

    elif table_name == "menu":
        cursor.execute("""INSERT INTO "menu" ("name","department_id") VALUES (%s, %s)""", (list[0], list[1]))

    elif table_name == "bookkeping":
        cursor.execute("""INSERT INTO "bookkeping" ("salary") VALUES (%s)""",(list[0]))

    elif table_name == "storage":
        cursor.execute("""INSERT INTO "storage" ("count_number") VALUES (%s)""",(list[0]))

    else:
        cursor.execute("""INSERT INTO "storage_department" ("kitchen_id","storage_id") VALUES (%s, %s)""",(list[0], list[1]))


def select_all(cursor, table_name):

    if table_name == "employeers":
        cursor.execute(""" SELECT 'Id', name, phone_number, position, concat(salary::numeric, '$') as salary, department_id from "employeers" """)
    if table_name == "quality_certificate":
        cursor.execute(""" SELECT 'Id', to_char(date_of_issue, 'YYYY-MM-DD'), to_char(expirition_date, 'YYYY-MM-DD'), authority_that_issued from "quality_certificate" """)
    else:
        cursor.execute(""" SELECT * FROM "{}" """.format(table_name))

    return cursor


def delete_one(cursor, table_name, pr_key):

    if table_name == "employeers":
        cursor.execute("""DELETE FROM "employeers" WHERE "Id" = %s """,(pr_key))
    elif table_name == "kitchen_department":
        cursor.execute("""DELETE FROM "kitchen_department" WHERE "Id" = %s """,(pr_key))
    elif table_name == "quality_certificate":
        cursor.execute("""DELETE FROM "quality_certificate" WHERE "Id" = %s """,(pr_key))
    elif table_name == "menu":
        cursor.execute("""DELETE FROM "menu" WHERE "Id" = %s """,(pr_key))
    elif table_name == "bookkeping":
        cursor.execute("""DELETE FROM "bookkeping" WHERE "Id" = %s """,(pr_key))
    elif table_name == "storage":
        cursor.execute("""DELETE FROM "storage" WHERE "Id" = %s """,(pr_key))
    elif table_name == "storage_department":
        cursor.execute("""DELETE FROM "storage_department" WHERE "Id" = %s """,(pr_key))

    return cursor.rowcount


def delete_all(cursor,table_name):
    cursor.execute("""DELETE FROM "{}" """.format(table_name))
    return cursor.rowcount


def update_item(cursor, table_name, list):
    if table_name == "employeers":
        cursor.execute("""UPDATE "employeers" SET "name" = %s, "phone_number" = %s, "position" = %s, "salary" = %s, "department_id" = %s
        WHERE "Id" = %s """, (list[1], list[2], list[3], list[4], list[5], list[0]))

    elif table_name == "kitchen_department":
        cursor.execute("""UPDATE "kitchen_department" SET "name_of_department" = %s, "employeers_count" = %s, "certificate_id" = %s, "book_id" = %s
        WHERE "Id" = %s """, (list[1], list[2], list[3], list[4], list[0]))
    
    elif table_name == "quality_certificate":
        cursor.execute("""UPDATE "quality_certificate" SET "date_of_issue" = %s, "expirition_date" = %s, "authority_that_issued" = %s
        WHERE "Id" = %s """, (list[1], list[2], list[3], list[0]))

    elif table_name == "menu":
        cursor.execute("""UPDATE "menu" SET "name" = %s, "department_id" = %s
        WHERE "Id" = %s """, (list[1], list[2], list[0]))

    elif table_name == "storage":
        cursor.execute("""UPDATE "storage" SET "count_number" = %s
        WHERE "Id" = %s """, (list[1], list[0]))

    else:
        cursor.execute("""UPDATE "storage_department" SET "kitchen_id" = %s, "storage_id" = %s
        WHERE "Id" = %s """, (list[1], list[2], list[0]))

    return cursor.rowcount


def connect_to_db():
    connection = psycopg2.connect(dbname=DBNAME, user=USERNAME, password=DBPASSWORD)
    return connection


def disconnect_from_db(connection,cursor):
    cursor.close()
    connection.close()
    print("Connection with Data Base is closed")

def random(cursor, value):
    cursor.execute(""" insert into "bookkeping" (salary)
        SELECT trunc(random()*1000)::int
FROM generate_series(1, %s) ; """, (value))



def static_search(cursor, table_name):

    cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' ORDER BY ORDINAL_POSITION")
    columns = cursor.fetchall()
    for i, elem in enumerate(columns):
        print(f"{i}.  {elem[0]}")
    while True:
        inp = input("enter column number:")
        if inp.isdecimal():
            inp = int(inp)
            break
    value = input("enter search value:")
    cursor.execute(SQL("SELECT * FROM {} WHERE" + f" {columns[inp][0]} = %s").format(Identifier(table_name)), (value,))
    return cursor
    
