from coapthon.resource_directory.resourceDirectory import ResourceDirectory


def main():
    server = ResourceDirectory("127.0.0.1", 5690, 'rdd')
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")


if __name__ == '__main__':
    main()