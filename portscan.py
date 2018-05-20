import sys
import socket

portas = [20, 21, 22, 23, 25, 42, 53, 67, 68, 80, 110, 119, 123, 143, 161, 389, 443, 445, 636, 666, 873, 993, 995, 1433, 3306, 3389, 5800, 5900, 8080]

argumentos = sys.argv

try:
	dominio = argumentos[1]
except:
	print("Faltou chamar o dominio como parametro")
	sys.exit(1)

for porta in portas:
	cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cliente.settimeout(1)
	codigo = cliente.connect_ex((dominio, porta))

	if codigo == 0:
		print porta, " Porta em uso!"
