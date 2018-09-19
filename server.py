import socketserver


HOST = 'localhost'
PORT = 5454
messages = []


class Message():
    msg1 = None
    msg2 = None
    msg3 = None

    def encoded(self):
        return self.msg1 + '#' + self.msg2 + '#' + self.msg3

    def checksum(self):
        return len(self.msg1 + self.msg2 + self.msg3)


class MyUDPHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        print('listening...')

        if self.server.data.msg1 is None:
            print('received 1')
            self.server.data.msg1 = self.request[0].decode()
        elif self.server.data.msg2 is None:
            print('received 2')
            self.server.data.msg2 = self.request[0].decode()
        elif self.server.data.msg3 is None:
            print('received 3')
            self.server.data.msg3 = self.request[0].decode()

            reply = self.server.data.encoded()
            checksum = str(self.server.data.checksum())

            print('sending reply:', reply)
            print('sending checksum:', checksum)

            self.request[1].sendto(reply.encode(), self.client_address)
            self.request[1].sendto(checksum.encode(), self.client_address)

            self.server.data = Message()



server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
server.data = Message()
server.serve_forever()