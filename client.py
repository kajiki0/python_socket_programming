#rode o client.py em outro lugar(terminal,cmd,...) pois o vscode(no meu caso) já esta rodando o servidor

import socket


HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
DISCONNECT_MESSAGE = "!DESCONECTADO"
ADDR = (SERVER,PORT)

#conectando o cliente
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

#função para mandar a mensagem
def send(msg):
    #isso aqui so aceita que da certo.
    '''
    É um conversao de colocar no formato da mensagem(utf-8)
    depois pega o tamanho da mensagem
    após isso convertemos para string o tamanho da mensagem e novamente colocamos no formato utf-8
    e faz uma conta para pegar a mensagem ja codificada somando com representação da string vazia em bytes multiplicado pelo tamanho fixo de bytes menos o tamanho da mensagem já convertida
    '''
    message = msg.encode(FORMAT) 
    msg_length = len(message)
    send_lenght = str(msg_length).encode(FORMAT)
    send_lenght = send_lenght + b' ' * (HEADER - len(send_lenght))
    
    client.send(send_lenght)
    client.send(message)
    #mostra a mensagem do servidor que definimos em server.py
    print(client.recv(2048).decode(FORMAT)) #numero grande o suficiente para lidar com a mensagem do servidor


send("MENSAGEM DO CLIENTE")
input()# apenas para esperar antes de mandar outra mensagem
send("MENSAGEM FINAL")


#vai desconectar pois foi a mensagem que definimos na função handle_client() para se desconectar
send(DISCONNECT_MESSAGE)


