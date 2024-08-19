import sys

from coapthon.resource_directory.resourceDirectory import ResourceDirectory


def main():
    is_drd = False
    rd_number = 30
    initial_port = 5550
    DRD_ports = []
    if(is_drd):
        for i in range(1, rd_number):
            DRD_ports.append(initial_port+i)

    server = ResourceDirectory("127.0.0.1", int(sys.argv[1]), sys.argv[2], isDRD=is_drd, DRD_ports=DRD_ports)
    try:
        print(sys.argv[1])
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")


if __name__ == '__main__':
    main()