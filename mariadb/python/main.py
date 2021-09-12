import pymysql

connection = None
cursor = None
query = ""

connection = pymysql.connect(host='localhost', port=3306, user='init', password='init123!!', db='project', charset='utf8')
cursor = connection.cursor()

sql = """
        CREATE TABLE IF NOT EXISTS
            test (
                id      char(4),
                name    char(10)
            )
    """

cursor.execute(sql)
connection.commit()
connection.close()
