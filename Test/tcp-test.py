import socket

s = socket.socket()
host = socket.gethostname()
port = 8888

s.connect((host, port))
print 'Connected to', host

while True:
    z = raw_input("Enter something for the server: ")
    s.send(z)
    # Halts
    print '[Waiting for response...]'
    print s.recv(1024)