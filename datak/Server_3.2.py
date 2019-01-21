                                        ## Ausama Askar
# Import socket module
from socket import *    

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 80

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

while True:
        print('Waiting for requests ...')
        # Set up a new connection from the client
        connectionSocket, addr = serverSocket.accept()
        # If an exception occurs during the execution of try clause
        # the rest of the clause is skipped
        # If the exception type matches the word after except
        # the except clause is executed
        try:
                message =  connectionSocket.recv(1024)
                # -------------------------------------------
                #       Request handling Section
                # -------------------------------------------
                data_received=message.split(b'\r\n')

                for i in range(len(data_received)): ##For loop to iterate through the message and
                        print(data_received[i])         ##print out every line in it.

                requested_resource = data_received[0]   ##requested_resource is now the first line in data_recieved
        
                requested_resource = requested_resource.split(b' ') #seperating the first line by "b" and blankspace to get every piece of information on its own
                requested_resource = requested_resource[1]
                
                print (requested_resource)
                
                f = open(requested_resource[1:],'rb')
                outputdata = f.read()
                connectionSocket.sendall(outputdata) 
                connectionSocket.close()


        except IOError:
                # ----------------------------------
                #       I/O Error handling
                # ----------------------------------
                        
                        connectionSocket.close()


        except IndexError:
                print('Index error exception')                          
serverSocket.close()                
                
                
        

