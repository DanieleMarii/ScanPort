# ScanPort
Um scanner de portas simples em Python que verifica a acessibilidade de portas comuns em um IP ou domínio informado, identificando quais estão abertas através de conexões TCP. Não utiliza o Nmap nem ferramentas externas, todo o processo de varredura é feito nativamente usando sockets do próprio Python.

---

## ✨ Visão Geral
O script faz a varredura de todas as portas (1-65535) de forma rápida com multithreading, detecta serviços conhecidos e aponta vulnerabilidades associadas. </br>
Os resultados são exibidos no terminal e também salvos em arquivos XML organizados em /var/log/port_scanner.

---

## ⚖️ Funcionalidades
- Escaneamento de portas TCP com alta performance (ThreadPoolExecutor)
- Detecção de serviços padrões (HTTP, FTP, SSH, etc.)
- Indicação de vulnerabilidades conhecidas (Heartbleed, EternalBlue, etc.)
- Relatórios gerados em:
- **XML**
- Salva logs automaticamente em /var/log/port_scanner/
- Progressão de varredura exibida no terminal

---

## 📝 Requisitos
- Python 3.7+
- Permissões de root para salvar logs em /var/log

---

# 🕹️ Como Usar 
```bash
sudo python3 portscanner.py
```

Você será solicitado a inserir:
- IP ou domínio do alvo

O scanner inicia a varredura e gera o relatório automaticamente.

---

## 🔎 O que o Script Faz
1. Solicita o IP ou domínio a ser escaneado
2. Escaneia todas as 65535 portas TCP usando conexões paralelas
3. Detecta serviços associados às portas abertas
4. Exibe vulnerabilidades relacionadas às portas identificadas
5. Gera um arquivo XML com os resultados no diretório de logs

---

## 📂 Estrutura do Relatório XML

```bash
<PortScannerReport>
  <Target>192.168.0.1</Target>
  <ScanDate>2025-04-28T14:30:00</ScanDate>
  <TotalOpenPorts>5</TotalOpenPorts>
  <OpenPorts>
    <Port>
      <Number>22</Number>
      <Service>SSH</Service>
      <Vulnerabilities>Brute Force SSH, Shellshock, Chaves fracas</Vulnerabilities>
    </Port>
    ...
  </OpenPorts>
</PortScannerReport>

```

---

## ❌ Encerramento Seguro
- Ctrl+C cancela a varredura de forma controlada
- Logs e conexões são finalizados corretamente

---

## 🚀 Casos de Uso
- Testes de segurança em redes privadas
- Auditoria de serviços expostos
- Detecção de vulnerabilidades comuns em ambientes internos

---

## 📄 Licença
Ferramenta de uso educativo.
> ⚠️ Utilize apenas em sistemas que você tenha autorização para escanear.


