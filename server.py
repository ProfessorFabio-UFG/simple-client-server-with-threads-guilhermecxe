from socket import socket, AF_INET, SOCK_STREAM
from constCS import HOST, PORT
from time import sleep

# Cria o socket e o associa ao endereço e porta especificados
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)           # Fica aguardando por conexões (máximo de uma conexão)

# Aceita a conexão de um cliente
(conn, addr) = s.accept()

print(f"Conexão estabelecida com {addr}")

while True:
	data = conn.recv(1024)  # Recebe até 1024 bytes de dados do cliente

	if not data:  # Se não houver dados (cliente fechou a conexão)
		break

    # Decodifica os dados recebidos
	command = bytes.decode(data).strip('"').split()
	if not command:
		break

	sleep(2)

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

# Fecha a conexão após o loop
conn.close()
print("Conexão encerrada.")
