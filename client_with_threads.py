import json
from socket import socket, AF_INET, SOCK_STREAM
from constCS import HOST, PORT
from threading import Thread
from time import time

def send_command(command):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((HOST, PORT))
        encoded_data = json.dumps(command).encode('utf-8')
        s.send(encoded_data)
        response = s.recv(1024)
        # print(f"Comando: {command} -> Resposta: {response.decode('utf-8')}")
        s.close()
    except Exception as e:
        print(f"Erro ao enviar comando {command}: {e}")

threads = []
start = time()

commands = [
    "sum 5 3",
    "sub 10 4",
    "mul 2 8",
    "div 16 4",
    "sum 1.5 2.5",
    "div 10 1",
    "mul 7 3.2",
    "sub 100 99",
    "sum -5 15",
    "div 18 3"
]

for command in commands:
    thread = Thread(target=send_command, args=(command,))
    threads.append(thread)
    thread.start()

# Aguarda todas as threads terminarem
for thread in threads:
    thread.join()

end = time()
print(f"Tempo total: {end - start:.2f} segundos")