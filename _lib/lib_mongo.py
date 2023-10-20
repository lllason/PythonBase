from pymongo import MongoClient

class MongoHandler:
    def __init__(self, conf):
        self.client = MongoClient(conf.mongo_uri)
        self.db = self.client[conf.db_name]
        self.collection = self.db[conf.collection] 

    def multi_insert_students(self, student_data_list):
        if student_data_list:
            self.collection.insert_many(student_data_list)

    def update_students(self, query, update_data):
        # 使用update_many執行多筆更新
        self.collection.update_many(query, {"$set": update_data})

    def delete_students(self, query):
        # 使用delete_many執行多筆刪除
        self.collection.delete_many(query)

    def find_all_students(self,query={}):
        cursor = self.collection.find(query)
        return [d for d in cursor]

    def insert_student(self, student_data):
        self.multi_insert_students([student_data])        