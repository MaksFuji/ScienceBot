from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import mysql.connector
from config import host, user, password, db_name, port
import traceback

### Здесь BirthDate, а в CreateFormHandler birth
### тоже самое с group и group_
slovar = {
    'log': 'INT',
    'name': 'TEXT',
    'description': 'TEXT',
    'photo': 'TEXT',
    'BirthDate': 'TEXT',
    'faculty': 'TEXT',
    'group_': 'TEXT',
    'course': 'INT',
    'phone': 'TEXT',
    'capitan': 'TEXT',
    'teammates': 'TEXT'
}


async def try_sub(list_name, log):
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        passwd=password,
        database=db_name
    )
    cursor = connection.cursor()
    try:
        querry = f'SELECT log FROM sublist{list_name} WHERE log = %s'
        cursor.execute(querry, [log])
        if cursor.fetchone() is not None:
            return 1
        else:
            return 404
    except Exception:
        print(traceback.format_exc())
    finally:
        connection.close()


async def create_sublist(list_name, columns):
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        passwd=password,
        database=db_name
    )
    cursor = connection.cursor()
    try:
        columns.append('log')
        table_name = 'sublist' + str(list_name)
        create_querry = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' ('
        arr = columns
        count = 0
        for i in range(1, len(arr)):  # КОСТЫЛЬ
            if i == len(arr) - 1:
                create_querry += arr[i] + ' ' + slovar[arr[i]] + ')'
                break
            match arr[i]:
                case 'teammates':
                    count = count + 1
                    create_querry += arr[i] + str(count) + ' ' + slovar[arr[i]] + ','
                case _:
                    create_querry += arr[i] + ' ' + slovar[arr[i]] + ','
        cursor.execute(create_querry)
        connection.commit()
        return 1
    finally:
        connection.close()


async def add_sub(list_name, columns, content):
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        passwd=password,
        database=db_name
    )
    cursor = connection.cursor()
    try:
        test_querry = f'SELECT log FROM sublist{list_name} WHERE log = %s'
        cursor.execute(test_querry, [content[0]])
        if cursor.fetchone() is not None:
            return 606
        else:
            table_querry = f'INSERT INTO sublist{list_name}('
            columns_arr = columns.split('/')
            for i in range(0, len(columns_arr)):
                if i == len(columns_arr) - 1:
                    table_querry += columns_arr[i] + ' ' + ') VALUES (' + ('%s,' * (len(columns_arr) - 1)) + '%s)'
                    break
                table_querry += columns_arr[i] + ','
            cursor.execute(table_querry, content)
            connection.commit()
    finally:
        connection.close()


async def extract_subs(list_name):
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        passwd=password,
        database=db_name
    )
    cursor = connection.cursor()
    try:
        table_name = 'sublist' + str(list_name)
        extract_querry = 'SELECT * FROM ' + table_name
        cursor.execute(extract_querry)
        if cursor.fetchone() is None:
            return 404
        else:
            return cursor.fetchall()
    finally:
        connection.close()


async def delete_sub(list_name, log):
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        passwd=password,
        database=db_name
    )
    cursor = connection.cursor()
    try:
        table_name = 'sublist' + str(list_name)
        find_querry = 'SELECT * FROM ' + table_name + ' WHERE log = %s'
        cursor.execute(find_querry, [log])
        if cursor.fetchone() is None:
            return 404
        else:
            delete_querry = 'DELETE FROM ' + table_name + ' WHERE log = %s'
            cursor.execute(delete_querry, [log])
            connection.commit()
            return 1
    finally:
        connection.close()

# async def delete_sublist(name):
#    connection = mysql.connector.connect(
#            host=host,
#            port = port,
#            user=user,
#            passwd=password,
#            database=db_name
#        )
#    cursor = connection.cursor()
#    try:
