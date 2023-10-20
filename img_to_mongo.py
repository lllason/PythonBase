from pymongo import MongoClient
from gridfs import GridFS
from PIL import Image
from io import BytesIO

# 连接到 MongoDB
client = MongoClient("mongodb://user01:11qqaazz@120.109.48.253")
db = client["images"]

# 获取 GridFS 对象
fs = GridFS(db)

# 读取图片并存储
with open("girl3.jpg", "rb") as image_file:
    image_data = image_file.read()
    fs.put(image_data, filename="girl3.jpg")

# 从 MongoDB 中检索图片
retrieved_image = fs.get_last_version(filename="girl3.jpg")
image_bytes = retrieved_image.read()

# 打开处理后的图像
processed_image = Image.open(BytesIO(image_bytes))

# 保存图像到文件
processed_image.save("processed_image_saved2.jpg")

# 关闭图像
processed_image.close()