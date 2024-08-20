import sys

from coapthon.defines import MONGO_DATABASE
from coapthon.resource_directory.resourceDirectory import ResourceDirectory


def main():
    isDRD = True
    rd_number = 30
    initial_port = 5550
    DRD_ports = []
    if(isDRD):
        for i in range(1, rd_number):
            DRD_ports.append(initial_port+i)
    server = ResourceDirectory("127.0.0.1", int(sys.argv[1]), MONGO_DATABASE, True, isDRD, DRD_ports, fuseki_port)
    try:
        print(sys.argv[1])
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")


if __name__ == '__main__':
    main()