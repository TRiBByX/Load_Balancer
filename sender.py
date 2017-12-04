import socket

try:
    TCP_IP = "192.168.0.27"
    TCP_PORT = 8080
    BUFFER_SIZE = 2048

    MESSAGE = str.encode(input())

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    while True:
        s.send(MESSAGE)
        # data = s.recv(BUFFER_SIZE)
        MESSAGE = str.encode(input())

    s.close
except KeyboardInterrupt:
    print("we ded")

# print("Data", data)
