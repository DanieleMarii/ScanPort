import socket
 
def scan_ports(target, ports):
    print(f"Escaneando {target}...\n")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Tempo limite para conexão
        result = sock.connect_ex((target, port))  # Tenta conectar
        if result == 0:
            print(f"[+] Porta {port} aberta")
        sock.close()
 
if __name__ == "__main__":
    alvo = input("Digite o IP ou domínio a ser escaneado: ")
    portas = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]  # Lista de portas comuns
    scan_ports(alvo, portas)
