from models import models
import socket
import thread


def instanceLoop():
    """A loop that keeps the tcp client running."""
    try:
        while True:
            tcpLoop()
    except KeyboardInterrupt:
        return None


def tcpLoop():
    """A TCP loop that handles incoming command calls."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8888
    print(host, port)
    s.bind((host, port))

    s.listen(1)
    c = None

    while True:
        if c is None:
            print('[No connection established]')
            c, addr = s.accept()
            print('[Connection established with: {}]'.format(addr))
        else:
            print('[Waiting for command...]')
            data = c.recv(1024)

                # TODO: Build command structure underneath.
            if data.decode() == 'get':
                c.send(str.encode('[getting...]'))
            else:
                c.send(str.encode('[Command not understood...]'))
