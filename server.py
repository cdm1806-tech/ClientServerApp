import socket

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server is waiting for connections...")

conn, addr = server.accept()

print(f"Connected by {addr}")

while True:
    message = conn.recv(1024).decode()

    if not message:
        break

    print("Client:", message)

    reply = input("Server: ")

    conn.send(reply.encode())

conn.close()
server.close()