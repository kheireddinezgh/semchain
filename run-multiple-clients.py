import subprocess

clients = ''
clients_number = 5
port = 5550
for x in range(clients_number-1):
    clients += " & python clientRD.py "+str(port)
    print(port)
    # port += 1
subprocess.run("python clientRD.py "+str(port)+clients, shell=True)