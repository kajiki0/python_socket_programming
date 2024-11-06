import socket
import threading


#definindo o tamanho da mensagem em bytes
#AVISO!: pode dar ruim escolhendo um valor fixo, pois uma mensagem que passe do tamanho pode quebrar algo e eu nao vou testar para dizer o que é esse "algo" ;) 
HEADER=64
#definindo a porta(uma que nao esteja sendo usada de preferencia ;D )
PORT = 5050

#definindo o formato da mensagem
FORMAT = 'utf-8'
#definir o server com o ip local do host(meu pc no caso)
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
DISCONNECT_MESSAGE = "!DESCONECTADO"
'''aqui definimos:
    -a familia do socket. Neste caso, o formato de endereço IP que vai aceitar
    -o tipo de socket.Neste caso, um socket para fluxo de dados no modelo client-server

obs: com o socket.socket() tambem podemos definir o numero de protocolo que por padrao é 0
'''
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#aqui estamos "ligando" o nosso endereço(ADDR) com o socket(server)
server.bind(ADDR)


def handle_client(connection,address):
    print(f"[NOVA CONEXAO] {address} conectado.")
    
    connected = True
    while connected:
        #recebe a mensagem do cliente
        
        '''
        Precisamos fazer um controle de fluxo na parte da mensagem, pois se servidor tentar receber 
        uma mensagem imediatamente do cliente, vai dar erro pois assim que se conecta uma mensagem "em branco" já é mandada e na hora de converter para inteiro acontece uns conflitos                                         (vou poupar minha cabeça agora e so aceitar que é isso ai que eu escrevi)
        '''
        message_lenght = connection.recv(HEADER).decode(FORMAT) #pega o tamanho
        if message_lenght: # se a mensagem estiver com o tamanho correto, entao continue
            message_lenght = int(message_lenght) #converte pra inteiro
            message = connection.recv(message_lenght).decode(FORMAT) #recebe a mensagem (parece mágica)

            #precisamos realizar a desconexao de uma forma mais limpa e visivel para nao dar problemas do tipo "o cliente realmente se desconectou?"
            if message==DISCONNECT_MESSAGE:
                connected=False
                
            print(f"[{address}] {message}")
            connection.send("Mensagem recebida pelo servidor".encode(FORMAT))
        
    #fecha a conexao
    connection.close()
        
#iniciar o socket 
def start():
    #colocando o socket para escutar ate 'alguem' 'bater' na porta
    server.listen()
    print(f"[LISTENING] O servidor esta escutando {SERVER}")
    while True:
        #server.accept() retorna uma tupla (connection, address) aceitando uma conexao.
        #como já sabemos,o socket tem que ser atrelado a um endereço e escutar/esperar por conexoes.Entao a variavel connection vai ser um novo objeto de socket
        #usavel para mandar e receber dados enquanto conectado e a variavel address é o endereço na outra ponta da conexao do socket para onde iremos mandar os dados
        connection,address = server.accept() 
        
        #iremos utilizar threads para lidar com as mensagens e conexoes do cliente pela função handle_client() enquanto o server esta conectado
        thread = threading.Thread(target=handle_client,args=(connection,address))
        thread.start()
        
        
        
        
        
        #ver quantas conexoes estao ativas
        #subtraia 1. o activeCount conta todas as threads nesse processo do python e a função que esta iniciando o server também é uma thread.Logo o que resta vao ser apenas os clientes(é o que queremos)
        print(f"\n[CONEXOES ATIVAS] {threading.active_count()-1}") 
        

print("[INICIANDO] Servidor esta iniciando...")
start()