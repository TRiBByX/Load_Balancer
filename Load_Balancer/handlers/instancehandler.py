from models import models
import socket
import thread


def instanceLoop():
    """Docstring."""
    while True:
        tcpLoop()


def tcpLoop():
    """Docstring."""
    try:
        TCP_IP = '192.168.0.27'
        TCP_PORT = 8080
        BUFFER_SIZE = 20

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP, TCP_PORT))
        s.listen(1)

        conn, addr = s.accept()
        print 'Connection Address: ', addr

        while True:
                data = conn.recv(BUFFER_SIZE)
                if not data: break
                print "Received data: ", data
                conn.send(data)
        conn.close()
    except socket.error:
        return None
