import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 5000

server_socket.bind((host, port))
server_socket.listen(1)

print("Waiting for client connection...")

client_socket, addr = server_socket.accept()
print("Connected to:", addr)

while True:
    client_message = client_socket.recv(1024).decode()
    print("Client:", client_message)

    if client_message.lower() == "bye":
        break

    message = input("Server: ")
    client_socket.send(message.encode())

    if message.lower() == "bye":
        break

client_socket.close()
server_socket.close()
