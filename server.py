import socket
# Define the quiz questions and answers
quiz = [
    {'question':'Which of the following transmission directions listed is not
a legitimate channel: Options are: Simplex \t Half Duplex \t Full Duplex \t
Double Duplex','answer':'Double Duplex'},
    {'question': 'What is the capital of France? Options are: Paris\t  New
York\t  Bengaluru \t  Venice', 'answer':'Paris'},
    {'question': 'What is the largest planet in the solar system? Options are:
Jupiter \t Saturn \t Uranus \t Neptune', 'answer': 'Jupiter'},
    {'question': 'What is the smallest country in the world? Options are:
Austria \t Germany \t Norway \t Vatican City ', 'answer':'Vatican City'}
     
]

# Set up the server
HOST = 192.168.100.14  # IP address of the host, to ensure connectivity.
PORT = 8001  # User defined port-> 1023
# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to a public host, and a well-known port
serversocket.bind((HOST, PORT))
# Become a server socket
serversocket.listen(1)
print('Quiz server is running on port', PORT)
# Wait for a connection, when connection is successful, proceed.
while True:
    print('Waiting for a connection...')
    (clientsocket, address) = serversocket.accept()
    print('Connection received from:', address)
    # Sending quiz questions to client
    count =0
    for question in quiz:
        clientsocket.send(question['question'].encode())
        # Receive answers from client
        answer = clientsocket.recv(1024).decode()
        if answer == question['answer']:
            clientsocket.send('Correct!'.encode())
            count+=1
         
           
        else:
            clientsocket.send('Incorrect!'.encode())
    print('Your score is:', count)
   
    # Close the connection
    clientsocket.close()
    print('Connection closed')
