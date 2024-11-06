# Estudo sobre redes de computadores e sockets com python

resumo do programa:

client.py manda mensagens pre-definidas para o servidor

server.py confirma que recebeu a mensagem com uma mensagem de confirmação no prompt do client.py

client.py manda uma mensagem para desconectar e se desconecta do servidor


## Algumas anotações que fiz:

### O que são sockets?
socket seria uma "ponta" de uma comunicação entre processos(um programa em execução,nesse caso) em uma rede

os processos podem estar na mesma maquina(unix socket) ou na rede de internet

obs:como a maioria da comunicação atual entre dispositivos se baseia no tcp/ip, então a maioria dos sockets sao 'TCP/IP sockets'

### porta x socket:
porta é uma identificação para um determinado protocolo ou serviço
socket é o ato da conexao em si, o fato de estar 'ligado', a comunicação dos processos
(veja o link do stackoverflow, a explicação mais votada é excelente e 'for dummies')

no modelo OSI, os sockets estao entre a camada 7(aplicação) e camada 6(transporte)



### O que sao threads?
em resumo: uma serie de comandos/instruções que integra um processo principal

processadores atuais tem a capacidade de suportar multitarefa simultanea, ou seja, multiplas threads sao processadas ao mesmo tempo para
otimizar o desempenho do sistema

obs: na prática, a execução das threads nao ocorre de forma verdadeira simultanea.Ainda é de forma sequencial, mas troca entre
threads tao rapido que parece simultaneo

certo, mas como utilizaremos no python?

tirando a parte mais "low level" da parada, aqui threads vao ser uma forma de executar tarefas concorrentemente.

entao a thread no python é uma linha de execução separada que pode ser executada simultaneamente com outras threads dentro do mesmo processo permitindo
que partes do programa sejam executados em simultaneamente(concorrentemente).
isso é util para operações de rede ou acessos a arquivos
(veja o link para um artigo no medium sobre threads em python, vale a pena!)


#


fonte principal:

[Python Socket Programming Tutorial - Tech with Tim](https://www.youtube.com/watch?v=3QiPPX-KeSc)


#

fontes extras para pesquisa e explicação de termos:

[introducao tcp,udp e sockets](https://www.treinaweb.com.br/blog/uma-introducao-a-tcp-udp-e-sockets)

[socket vs porta - stackoverflow](https://pt.stackoverflow.com/questions/277758/qual-%C3%A9-a-diferen%C3%A7a-entre-socket-e-porta)

[threads](https://www.hardware.com.br/artigos/entenda-o-que-sao-as-threads-dos-processadores/)

[doc do python sobre sockets](https://docs.python.org/3/library/socket.html)

[threads em python - medium](https://medium.com/@habbema/threads-em-python-9a3a7b3c776d)

[programação concorrente](https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_concorrente)