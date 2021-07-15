from django.db import connection
from contextlib import closing


def check_user():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select username,password from login_sign_in""")
        course = dict_fetchall(cursor)
        return course

def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
