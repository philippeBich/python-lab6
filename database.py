import pymysql
import json

def getTasksId():

    sql = "SELECT id_task FROM tasks"

    conn = pymysql.connect(user='root', password='root',
                           database='lab6', host='localhost')
    cursor = conn.cursor()
    cursor.execute(sql)

    row = cursor.fetchall()
    L = []
    conn.close()

    for x in row:
        L.extend(x)

    return L

def getText(id):
    sql = "SELECT text FROM tasks where id_task=%s"

    conn = pymysql.connect(user='root', password='root',
                           database='lab6', host='localhost')
    cursor = conn.cursor()
    cursor.execute(sql, (id,))

    row = cursor.fetchone()[0]
    conn.close()


    return row


def getUrgency(id):
    sql = "SELECT urgent FROM tasks where id_task=%s"

    conn = pymysql.connect(user='root', password='root',
                           database='lab6', host='localhost')
    cursor = conn.cursor()
    cursor.execute(sql, (id,))

    row = cursor.fetchone()[0]
    conn.close()

    return row

def insertTask(task):
    sql = "insert into tasks ( text, urgent) values ( %s, %s)"

    conn = pymysql.connect(user='root', password='root',
                           database='lab6', host='localhost', autocommit=True)
    cursor = conn.cursor()
    cursor.execute(sql, (task['text'],task['urgency']))
    conn.close()

def deleteTask(task):
    sql="delete from tasks where id_task=%s"

    conn = pymysql.connect(user='root', password='root',
                           database='lab6', host='localhost', autocommit=True)
    cursor = conn.cursor()
    cursor.execute(sql, (task['name'],))
    conn.close()

def updateTask(task):
    sql="update tasks set text=%s, urgent=%s where id_task=%s"

    conn = pymysql.connect(user='root', password='root',
                           database='lab6', host='localhost', autocommit=True)
    cursor = conn.cursor()
    cursor.execute(sql, (task['text'],task['urgency'], task['name']))
    conn.close()