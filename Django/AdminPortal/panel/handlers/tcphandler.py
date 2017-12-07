import socket
import ast

def tcp_connection(command):
    s = socket.socket()
    host = socket.gethostname()
    port = 8888
    s.connect((host, port))
    s.send(command)
    context = {'servers': ast.literal_eval(s.recv(1024))}
    s.close()
    print 'closed connection'
    return context