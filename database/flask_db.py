import sqlite3


def select_data(login):
    db_lp = sqlite3.connect(r'database/FlaskAppUsers.db')

    cursor_db = db_lp.cursor()
    #sql_select = ("""SELECT password FROM users_data WHERE username = '{}'""").format(login)

    result = cursor_db.execute(("""SELECT password FROM users_data WHERE username = '{}'""").format(login))

    db_lp.commit()
    #db_lp.close()

    return result.fetchone()


def insert_data(login, password):
    db_lp = sqlite3.connect(r'database/FlaskAppUsers.db')

    cursor_db = db_lp.cursor()
    sql_insert = ("""INSERT INTO users_data(username, password) VALUES('{}','{}')""").format(login, password)

    cursor_db.execute(sql_insert)

    cursor_db.close()

    db_lp.commit()
    db_lp.close()
