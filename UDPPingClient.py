import socket
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'Testing Ping'

for i in range(10):
    try:
        # Send data
        print("Ping ", i + 1, time.time())
        sent = sock.sendto(message.encode(), server_address)
        start = time.time()
        # Receive response
        # print('Waiting to receive message from server')
        sock.settimeout(1)
        data, server = sock.recvfrom(4096)
        end = time.time()
        print('RTT for Packet %s is %s \n' % (i + 1, start - end))
    except socket.timeout as e:
        print("Request timed out \n")

print('10 Packets have been sent, Closing socket!')
sock.close()
