
import mysql.connector
from config_data import config

async def add_qq(columns, content):
    connection = mysql.connector.connect(
            host=config.db.db_host,
            port=config.db.port,
            user=config.db.db_user,
            passwd=config.db.db_password,
            database=config.db.database
        )
    cursor = connection.cursor()
    try:
        if len(columns) - len(content) != 0:
            return 808
        cursor.execute('SELECT * FROM qq_list WHERE for_id = %s', [content[0]])
        if cursor.fetchone() is not None:
            return 606
        length = len(content)
        columns_arr = columns
        add_querry = f'INSERT INTO qq_list ('
        for i in range(0, length):
            if i == length-1:
                add_querry += f'for_{columns_arr[i]}) VALUES (' + '%s,'*(length-1) + '%s)'
                break
            add_querry += f'for_{columns_arr[i]}, '
        cursor.execute(add_querry,content) 
        connection.commit()
        return 1
    finally:
        connection.close()


async def extract_qq(id_):
    connection = mysql.connector.connect(
            host=config.db.db_host,
            port=config.db.port,
            user=config.db.db_user,
            passwd=config.db.db_password,
            database=config.db.database
        )
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * FROM qq_list WHERE for_id = %s', [id_])
        res = cursor.fetchone()
        if res is None:
            return 404
        else:
            qq_arr = []
            for i in range (0, len(res)):
                if res[i] is not None:
                    qq_arr.append(res[i])
            return qq_arr
    finally:
        connection.close()

