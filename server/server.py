import socket
import threading

HEADER = 64
PORT = 7070 #port for testing purposes only
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[New Connection] {addr} connected")

    connected = True
    while connected:
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)
            if msg == '!DISCONNECT':
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()
    
                

def start():
    server.listen()
    print(f"[SERVER] Started up listening on {HOST} port {PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[SERVER] Active connections: {threading.active_count() - 1}")


print("[SERVER] Starting server...")
start()