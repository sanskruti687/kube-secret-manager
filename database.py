import MySQLdb

def connect_db():
    return MySQLdb.connect(
        host="172.27.107.31",
        user="root",
        password="Sanskruti@123",
        database="internship_db"
    )
