import json

# 读取 JSON 文件
with open('pose.json', 'r') as file:
    # 从文件加载 JSON 数据
    data = json.load(file)

# 打印字典数据
print(data)
# 访问特定键值对
X = data["X"]
Y = data["Y"]
Z = data["Z"]
RX = data["RX"]
RY = data["RY"]
RZ = data["RZ"]
Move = "({}, {}, {}, {}, {}, {})".format(X, Y, Z, RX, RY, RZ)
print(type(Move))

Ha = "(1,-335.94,-70.24,-34.49,-107.05,-88.72,17.97)"
print(type(Ha))

