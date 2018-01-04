import socket
import ast
import unittest
import instancehandler


class TestTCP(unittest.TestCase):

    def test_TCP(self):
        instancehandler.instanceLoop()

        s = socket.socket()
        host = socket.gethostname()
        port = 8888

        s.connect((host, port))

        s.send('message')
        self.assertEqual(s.recv(1024), 'Not Understood')
