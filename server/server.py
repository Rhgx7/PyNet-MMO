import socket
import threading

PORT = 7070 #port for testing purposes only
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[New Connection] {addr} connected")

    CONNECTED = True
    while CONNECTED:
        msg = conn.rcv() 

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")


print("Starting server")
start()