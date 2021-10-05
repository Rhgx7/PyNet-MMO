import socket

HEADER = 64
PORT = int(input("port: "))
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = input("server: ")
ADDR = (SERVER, PORT)



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(f"connected to {ADDR}")


def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(msg)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)

while True:
    send(input())