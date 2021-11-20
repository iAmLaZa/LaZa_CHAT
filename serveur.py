import socket
import threading

# Connection Data
host = '127.0.0.1'
port = 5010

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

users = []#tableau de user
pseudos = []#tableau des pseudos

def envoyer(message):
    for user in users:
        user.send(message)


def ecrire(user):
    while True:
        try:
            
            message = user.recv(1024)
            envoyer(message)
        except:
            
            index = users.index(user)
            users.remove(user)
            user.close()
            pseudo = pseudos[index]
            envoyer('{} left!'.format(pseudo).encode('ascii'))
            pseudos.remove(pseudo)
            break


def connection():
    while True:
        # Accept Connection
        user, address = server.accept()
        print(" user connectée est :  ")

   
        user.send('ps'.encode('ascii'))
        pseudo = user.recv(1024).decode('ascii')
        pseudos.append(pseudo)
        users.append(user)

        
        print(" {}".format(pseudo))
        envoyer(" {} joined!".format(pseudo).encode('ascii'))
        user.send('Connected to server!'.encode('ascii'))

        
        thread = threading.Thread(target=ecrire, args=(user,))
        thread.start()

print("serveur est en ecoute")
connection()



