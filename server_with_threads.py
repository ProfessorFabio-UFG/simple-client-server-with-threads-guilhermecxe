from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from time import sleep
from constCS import HOST, PORT

def handle_client(conn, addr):
    print(f"Conexão estabelecida com {addr}")
    while True:
        data = conn.recv(1024)  # recebe até 1024 bytes de dados do cliente, bloqueando até que o cliente envie dados

        if not data:  # se não houver dados (cliente fechou a conexão)
            break

        sleep(2)  # simula tempo de processamento

        # Decodifica os dados recebidos
        command = bytes.decode(data).strip('"').split()
        if not command:
            break

        if command[0] == "sum":
            result = float(command[1]) + float(command[2])
            response = f"{result}"
        elif command[0] == "sub":
            result = float(command[1]) - float(command[2])
            response = f"{result}"
        elif command[0] == "mul":
            result = float(command[1]) * float(command[2])
            response = f"{result}"
        elif command[0] == "div":
            result = float(command[2]) / float(command[1])
            response = f"{result}"

        # Envia a resposta para o cliente
        conn.send(str.encode(response))
    conn.close()
    print(f"Conexão encerrada com {addr}")

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3) # permite até 3 conexões simultâneas

print(f"Servidor escutando em {HOST}:{PORT}")

while True:
    conn, addr = s.accept() # bloqueia até que um cliente se conecte
    thread = Thread(target=handle_client, args=(conn, addr))
    thread.start()