import unittest
from _lib.lib_mongo import MongoHandler
from _conf.server_setting import ServerSettings

# 建立 ServerSettings 
settings = ServerSettings()  # 切换到 'dev' 或 'prod'

# 取得 MongoDB 設置內容
mongo_config = settings.get_mongo_config(settings.site_mode)
mongo_config["collection"] = "unitest_student"

class TestMongoHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("--- setUpClass")
        # 初始執行
        cls.mongo_handler = MongoHandler(mongo_config)
        cls.mongo_handler.delete_students({})

    @classmethod
    def tearDownClass(cls):
        print("--- tearDownClass")
        # 在整个测试类结束后执行一次
        cls.mongo_handler.client.close()

    def test_insert_student(self):
        print(".test_insert_student")
        cSource = "single_insert"
        student_data = { "name": "TestStudent", "student": "123456", "source": cSource }

        # 插入學生數據
        self.mongo_handler.insert_student(student_data)

        # 檢查是否成功插入
        inserted_student = self.mongo_handler.collection.find_one({"name": "TestStudent","source": cSource})
        self.assertIsNotNone(inserted_student)
        self.assertEqual(inserted_student["name"], "TestStudent")
        self.assertEqual(inserted_student["student"], "123456")

    def test_multi_insert_students(self):
        print(".test_multi_insert_students")
        cSource = "multi_insert"
        student_data_list = [
            {"name": "Student1", "student": "123456","source": cSource},
            {"name": "Student2", "student": "789012","source": cSource},
        ]

        # 调用multi_insert_students方法
        self.mongo_handler.multi_insert_students(student_data_list)

        # 检查是否成功插入
        inserted_students = self.mongo_handler.find_all_students({"source": cSource})
        self.assertEqual(len(inserted_students), len(student_data_list))

    def test_update_students(self):
        print(".test_update_students")
        # 创建一个测试用例：更新所有学生的数据
        query = {}  # 空查询表示更新所有学生
        update_data = {"status": "updated"}

        # 调用update_students方法
        self.mongo_handler.update_students(query, update_data)

        # 检查更新是否成功
        updated_students = self.mongo_handler.find_all_students()
        for student in updated_students:
            self.assertEqual(student["status"], "updated")

    def test_delete_students(self):
        print("test_delete_students")
        # 创建一个测试用例：删除所有学生的数据
        query = {}  # 空查询表示删除所有学生

        # 调用delete_students方法
        self.mongo_handler.delete_students(query)

        # 检查是否成功删除
        deleted_students = self.mongo_handler.find_all_students()
        self.assertEqual(len(deleted_students), 0)        

if __name__ == "__main__":
    unittest.main()