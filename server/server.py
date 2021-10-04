import socket
import threading

PORT = 7070 #port for testing purposes only
HOST = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
