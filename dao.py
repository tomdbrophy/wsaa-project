import pymysql
import pymysql.cursors

conn = pymysql.connect(user='root', cursorclass=pymysql.cursors.DictCursor, password='root', host='localhost', db='room_booking', port=3306)

query = 'SELECT * FROM locations'

with conn:
    cursor = conn.cursor()
    cursor.execute(query)
    locations = cursor.fetchall()
    for l in locations:
        print(l['Name'])


