import cv2
import socket

# 创建Socket客户端
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到远程Socket服务器
server_address = ('127.0.0.1', 12345)  # 替换为远程Socket服务器的IP和端口
client_socket.connect(server_address)

# # 从摄像头获取图像（同样以摄像头索引0为例）
# cap = cv2.VideoCapture(0)
# ret, frame = cap.read()

image_path = 'man.jpg'
frame = cv2.imread(image_path)

# 将图像编码为字节流
encoded_image = cv2.imencode('.jpg', frame)[1].tobytes()

# 发送图像数据
client_socket.sendall(encoded_image)

# 关闭Socket连接
client_socket.close()

# 关闭摄像头
#cap.release()