import subprocess

rds = ''
rd_number = 30
port = 5550
database = "RD"+str(port)
for x in range(rd_number-1):
    rds += " & python rd.py "+str(port)+" "+database
    port += 1
    database = "RD" + str(port)
print("python rd.py "+str(port)+" "+database+rds)
subprocess.run("python rd.py "+str(port)+" "+database+rds, shell=True)