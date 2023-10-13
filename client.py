import socket

# Set up the client
HOST = '192.168.100.14'  # The server's hostname or IP address
PORT = 8001  # The port used by the server

# Create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
clientsocket.connect((HOST, PORT))

# Initialize the score
score = 0

# Receive quiz questions from the server
for i in range(4):
    question = clientsocket.recv(1024).decode()
    print(question)
    answer = input('Enter your answer: ')
    clientsocket.send(answer.encode())
    response = clientsocket.recv(1024).decode()
    print(response)
    # Update the score based on the response
    if response == 'Correct!':
        score += 1

# Display the final score
print("Quiz completed!")
print("Your score: {}/4".format(score))

# Close the connection
clientsocket.close()
