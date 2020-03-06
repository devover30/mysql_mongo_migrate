import pymongo
import mysqlConnect

class MongoDB:

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

    def mysqlToMongo(self,dbName,collectionName,documents):
        db = self.client[dbName]
        collection = db[collectionName]
        ack = collection.insert_many(documents).acknowledged
        print(ack)

def main():
    mongodbName = ''
    mysqldb = mysqlConnect.main()
    tableNames = mysqldb.getAllTables()
    mongoConn = MongoDB()
    for table in tableNames:
        mysqldbData = mysqldb.selectTable(table)
        dataList = []
        for data in mysqldbData:
            dataDict = {'_id': data.getID(),'type':data.getType()}
            dataList.append(dataDict)
        mongoConn.mysqlToMongo(mongodbName,table,dataList)





if __name__ == '__main__':
    main()

