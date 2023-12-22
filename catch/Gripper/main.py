import time
import socket
import serial
import json

with open('pose.json', 'r') as file:
    # 从文件加载 JSON 数据
    data = json.load(file)
print(data)
X = data["X"]
Y = data["Y"]
Z = data["Z"]
RX = data["RX"]
RY = data["RY"]
RZ = data["RZ"]
Move = "({}, {}, {}, {}, {}, {}, {})".format(1, X, Y, Z, RX, RY, RZ)
print(Move)

x = serial.Serial('COM3', 115200, timeout=5000)
tcp_server_socket = socket.socket()
tcp_server_socket.bind(("192.168.8.144", 9999))
tcp_server_socket.listen(128)
conn_socket, ip_port = tcp_server_socket.accept()
print("客户端已连接：", ip_port)

init = "(1,-335.94,-70.24,-34.49,-107.05,-88.72,17.97)"
place = "(1,-371,117.69,170.30,-107.05,-88.72,17.97)"
# 开
c = '09 10 03 E8 00 03 06 09 00 00 00 FF FF 72 19'
# 关
a = '09 10 03 E8 00 03 06 09 00 00 FF FF FF 42 29'

time.sleep(20)
# 初始位姿
conn_socket.send(init.encode(encoding='utf-8'))
d = bytes.fromhex(c)
x.write(d)
time.sleep(1)

# 抓取位姿
conn_socket.send(Move.encode(encoding='utf-8'))
time.sleep(2)
b = bytes.fromhex(a)
x.write(b)
time.sleep(1)

# 初始位姿
conn_socket.send(init.encode(encoding='utf-8'))
time.sleep(2)

# 放置位姿
conn_socket.send(place.encode(encoding='utf-8'))
time.sleep(2)
d = bytes.fromhex(c)
x.write(d)
time.sleep(1)

# 初始位姿
conn_socket.send(init.encode(encoding='utf-8'))
time.sleep(2)