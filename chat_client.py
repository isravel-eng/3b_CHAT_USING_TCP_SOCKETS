import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 5000

client_socket.connect((host, port))
print("Connected to server")

while True:
    message = input("Client: ")
    client_socket.send(message.encode())

    if message.lower() == "bye":
        break

    server_message = client_socket.recv(1024).decode()
    print("Server:", server_message)

    if server_message.lower() == "bye":
        break

client_socket.close()
