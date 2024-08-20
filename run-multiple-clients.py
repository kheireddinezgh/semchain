import random
import subprocess

clients = ''
clients_number = 20
rd_number = 6
for x in range(clients_number-1):
    rd_ = random.randint(0, rd_number - 1)
    port = 5550 + rd_
    clients += " & /home/iot/PycharmProjects/drdchain/venv/bin/python clientRD.py "+str(port)
    print(port)
    # port += 1
subprocess.run("/home/iot/PycharmProjects/drdchain/venv/bin/python clientRD.py "+str(port)+clients, shell=True)