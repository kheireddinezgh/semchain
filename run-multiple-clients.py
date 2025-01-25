import random
import subprocess

clients = ''
clients_number = 15
rd_number = 6
port = 5551
for x in range(clients_number-1):
    # rd_ = random.randint(0, rd_number - 1)
    # port = 5551 + rd_
    port = 5551 + (x % rd_number)
    clients += " & /home/iot/PycharmProjects/drdchain/venv/bin/python clientRD.py "+str(port)
    print(port)
    # port += 1
subprocess.run("/home/iot/PycharmProjects/drdchain/venv/bin/python clientRD.py "+str(port)+clients, shell=True)