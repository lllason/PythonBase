import socket

# 创建Socket服务器
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 定义服务器地址和端口
server_address = ('0.0.0.0', 12345)  # 使用0.0.0.0可以监听所有网络接口
server_socket.bind(server_address)

# 开始监听传入的连接请求
server_socket.listen(5)

print("等待连接...")

while True:
    # 接受客户端的连接
    client_socket, client_address = server_socket.accept()

    print(f"接受来自 {client_address} 的连接")

    # 接收图像数据
    image_data = b''
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        image_data += chunk

    # 将接收到的图像数据保存到文件
    with open('received_image.jpg', 'wb') as image_file:
        image_file.write(image_data)

    print("图像数据已保存")

    # 关闭客户端连接
    client_socket.close()

# 关闭服务器Socket
server_socket.close()