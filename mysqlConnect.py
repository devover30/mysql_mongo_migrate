import mysql.connector

class PaymentEntity:

    def __init__(self,id,type):
        self.id = id
        self.type = type


    def __str__(self):
        return f'{self.getID(),self.getType()}'

    def getID(self):
        return int(self.id.decode())

    def getType(self):
        return self.type.decode()



class MysqlDB:

    def __init__(self):
        self.cnx = mysql.connector.connect(host='', user='', password='', database='')
        self.crs = self.cnx.cursor(raw=True)

    def selectTable(self,tableName):
        self.crs.execute(f'SELECT * FROM {tableName}')
        rows = self.crs.fetchall()
        newRows = []
        for row in rows:
            payment = PaymentEntity(row[0],row[1])
            newRows.append(payment)
        return newRows

    def getAllTables(self):
        self.crs.execute('SHOW TABLES')
        tables = self.crs.fetchall()
        newTables = []
        for table in tables:
            newTables.append(table[0].decode())
        return newTables


def main():
    database = MysqlDB()
    return database


if __name__ == '__main__':
    main()

