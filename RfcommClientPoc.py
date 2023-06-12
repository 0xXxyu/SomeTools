import bluetooth

# linux 环境

# sers = bluetooth.find_service(uuid='',address='')

# if len(sers) != 0:
#     port = sers["port"]
#     addr = sers["host"]
#     socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#     print("connect to "+addr)
#     socket.connect((addr,port))

#     data1 = bytes.fromhex('587879757465737431')
#     print("send data: "+data1)
#     socket.send(data1)

#     data2 = bytes.fromhex('587879757465737432')
#     print("send data: "+data2)
#     socket.send(data2)

#     socket.close()

addr = ''
port = 
socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("connect to "+addr.upper())
socket.connect((addr,port))

data1 = bytes.fromhex('587879757465737431')
print("send data: "+str(data1))
socket.send(data1)

data2 = bytes.fromhex('587879757465737432')
print("send data: "+str(data2))
socket.send(data2)

socket.close()
