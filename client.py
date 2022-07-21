import socket


port = 6803
host = 'localhost'

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#connecto the server
server.connect((host, port))

print("Welcome!, Enter message to send: ")
print("Please type /q to quit")
msg = input()
server.send(msg.encode())

while True:
    server.send(msg.encode()) #send a message
    response = server.recv(2048).decode() # response from server
    print("$ ", response)
    if msg == "/q":
        server.send(msg.encode())
        print("\n")
        break
    # enter input
    msg = input()

#close socket
server.close()




# -------Sources-----------------------------------------------------------------
# Jame kurose,Keith Ross computer networking:a top down approach Ch.2-7
# docs.python.org/3/howto/sockets.html#creating-a-socket












