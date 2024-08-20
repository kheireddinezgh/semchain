import subprocess

rds = ''
rd_number = 6
port = 5550
database = "RD"+str(port)
for x in range(rd_number-1):
    rds += " & /home/iot/PycharmProjects/drdchain/venv/bin/python rd.py "+str(port)+" "+database
    port += 1
    database = "RD" + str(port)
print("/home/iot/PycharmProjects/drdchain/venv/bin/python rd.py "+str(port)+" "+database+rds)
subprocess.run("/home/iot/PycharmProjects/drdchain/venv/bin/python rd.py "+str(port)+" "+database+rds, shell=True)