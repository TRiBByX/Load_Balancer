from models import models
from handlers import vmhandler
import socket
import threading
import json


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
            if not data:
                break

            data = data.split(' ')
            if data[0] == 'get':
                print 'I GOTS IT!'
                data = vmhandler.get_dict()
                print(data)
                jsondata = json.dumps(data)
                c.sendall(jsondata)
            elif data[0] == 'post':
                if data[1] == 'shutdown':
                    pass
                elif data[1] == 'start':
                    pass

                print 'post'

