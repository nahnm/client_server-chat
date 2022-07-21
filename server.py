import socket



port = 6803
host = 'localhost'
#create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind the server to the localhost and the port
server.bind((host, port))



server.listen(1)
print("Server is listening on: ", host, "\n", "port: ", port)
conn, addr = server.accept()
print(addr, " connected")

msg = conn.recv(2048).decode()
print("Hello! please type /q to quit")

# talking to client, receive data from client
while True:
    msg = conn.recv(2048).decode()

    if not msg:
        break
    print("/ ", str(msg))
    msg = input()
    # send data to client
    conn.send(msg.encode())
    if msg == "/q":
        message = "Chat ended, Farewell...!"
        conn.send(message.encode())
        print('\n')
        break

 #close connection
conn.close()





#-------Sources-----------------------------------------------------------------
#Jame kurose,Keith Ross computer networking:a top down approach Ch.2-7
#docs.python.org/3/howto/sockets.html#creating-a-socket

