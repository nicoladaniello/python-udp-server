import socket
import time

HOST = 'localhost'
PORT = 5454

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

t1 = input('ENTER MESSAGE 1:\n')
t2 = input('ENTER MESSAGE 2:\n')
t3 = input('ENTER MESSAGE 3:\n')
message = t1 + t2 + t3
checksum = len(message)

sock.sendto(t1.encode(), (HOST, PORT))
sock.sendto(t2.encode(), (HOST, PORT))
sock.sendto(t3.encode(), (HOST, PORT))

recv_message = ''
recv_checksum = ''

while len(recv_message) == 0 : recv_message = sock.recv(50).decode()
while len(recv_checksum) == 0 : recv_checksum = sock.recv(50).decode()

if (recv_message.replace('#', '') == message): print('message is correct! sent:', message, ', received:', recv_message)
else: print('message is wrong', recv_message)

if (int(recv_checksum) == checksum): print('checksum is correct! sent:', checksum, ', received:', recv_checksum)
else: print('checksum is wrong', recv_checksum)
