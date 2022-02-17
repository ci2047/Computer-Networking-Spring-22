# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(("", port))
  #Fill in start
  #Everything that needs to be said here to make it listen
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    #print('Ready to serve...')
    #Fill in start 
    connectionSocket, addr = serverSocket.accept()     
    #need to accept whatever is inbound -see powerpoint 

       #Fill in end
    try:

      try:
        
        message = connectionSocket.recv(1024).decode()

        #I have this file or I don't have this file
        
          #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        #Fill in start #read content of that file and send it  
        outputdata = f.read()
        f.close()
        #print(outputdata)
        #connectionSocket.sendall(outputdata.encode())
        #Fill in end
        
        #Send one HTTP header line into socket.
        #Fill in start
        connectionSocket.sendall('HTTP/1.1 200 OK'.encode())

        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start
       connectionSocket.sendall('HTTP/1.1 404 Not Found'.encode())

        #Fill in end


        #Close client socket
        #Fill in start
      connectionSocket.close() #close connection not the socket

        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
