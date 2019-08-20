from socket import *
import ssl
import base64
msg = "\r\n Hey, I just wanted to say that this lab is complete"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com", 587)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[0:3] != '220':
    print('220 reply not received from server.')

# Send EHLO command and print server response.
ehloCommand = 'EHLO Alice\r\n'
clientSocket.send(ehloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send STARTTLS command to server and print server response
command = "STARTTLS\r\n"
clientSocket.send(command.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[0:3] != '220':
    print('220 reply not received from server.')

# SSL Encryption
ssl_clientSocket = ssl.wrap_socket(clientSocket)

# Log On
authLogin = "AUTH LOGIN\r\n"
ssl_clientSocket.send(authLogin.encode())
recv1 = ssl_clientSocket.recv(1024).decode()
print(recv1)

if recv1[0:3] != '334':
    print('334 reply not received from server.')

# Send username credentials
username = "joemercodes@gmail.com"  # base64.b64encode("jramos07@manhattan.edu") + base64.b64encode('\r\n')
ssl_clientSocket.send(base64.b64encode(username.encode()) + "\r\n".encode())

recv1 = ssl_clientSocket.recv(1024).decode()
print(recv1)
if recv1[0:3] != '334':
    print('334 reply not received from server.')

# Send password credentials
password = "Jeba1016"  # base64.b64encode("Jeba1016") + '\r\n'
ssl_clientSocket.send(base64.b64encode(password.encode()) + "\r\n".encode())
recv1 = ssl_clientSocket.recv(1024).decode()
print(recv1)
if recv1[0:3] != '235':
    print('235 reply not received from server.')

# Send Mail From command
mailFrom = "MAIL FROM: <joemercodes@gmail.com>\r\n"
ssl_clientSocket.send(mailFrom.encode())
recv1 = ssl_clientSocket.recv(1024).decode()
print(recv1)
if recv1[0:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command
rcptCommand = "RCPT TO: <jramos07@manhattan.edu>\r\n"
ssl_clientSocket.send(rcptCommand.encode())
recv1 = ssl_clientSocket.recv(1024).decode()
print(recv1)
if recv1[0:3] != '250':
    print('250 reply not received from server.')

# Send DATA command
dataCommand = "DATA\r\n"
ssl_clientSocket.send(dataCommand.encode())
recv1 = ssl_clientSocket.recv(1024).decode()
print(recv1)
if recv1[0:3] != '250':
    print('250 reply not received from server.')

# Send message data
ssl_clientSocket.send(msg.encode())

# End Message
ssl_clientSocket.send(endmsg.encode())
recv1 = ssl_clientSocket.recv(1024).decode()
print(recv1)
if recv1[0:3] != '250':
    print('250 reply not received from server.')

# Send QUIT response
quitCommand = 'QUIT\r\n'
ssl_clientSocket.write(quitCommand.encode())
recv1 = ssl_clientSocket.read(1024)
print(recv1)
if recv1[0:3] != '221':
    print('221 reply not received from server.')

clientSocket.close()