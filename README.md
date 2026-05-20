# 3b.CREATION FOR CHAT USING TCP SOCKETS

## AIM
To write a Python program for creating Chat using TCP Socket Links.

## ALGORITHM
1. Import the necessary modules in Python.
2. Create a socket connection using the socket module.
3. Bind the server to an IP address and port number.
4. Listen for incoming client connections.
5. Accept the client connection from the server.
6. Send messages to the client and receive messages from the client using socket functions.
7. Use the send() and recv() functions for communication.
8. Close the socket connection after communication ends.

## PROGRAM

### chat_server.py
```python
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
```

### chat_client.py
```python
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
```

## OUTPUT

### Server Side
```text
Waiting for client connection...
Connected to: ('127.0.0.1', 54321)
Client: Hello
Server: Hi
Client: How are you?
Server: Fine
```

### Client Side
```text
Connected to server
Client: Hello
Server: Hi
Client: How are you?
Server: Fine
```

## RESULT
Thus, the Python program for creating Chat using TCP Socket Links was successfully executed.
