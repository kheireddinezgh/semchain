import random
import sys

from coapthon.client.helperclient import HelperClient
from coapthon import defines

def main():
    host = "127.0.0.1"
    # ports = [5683, 5690]
    # port = random.choice(ports)

    # Test discover
    # path = "/.well-known/core"
    # response = client.get(path)
    # print(response.pretty_print())

    # Create a registration resource
    # for x in range(10):
    # rd_number = 6
    # rd_ = random.randint(0, rd_number - 1)
    # port = 5551 + rd_
    # port = 5552
    # port = int(sys.argv[1])
    # client = HelperClient(server=(host, port))
    # for x in range(30):
    #     rd_number = 6
    #     rd_ = random.randint(0, rd_number - 1)
    #     port = 5551 + rd_
    #     client = HelperClient(server=(host, port))
    #     if_name = 'sensor'
    #     resource_number = 1
    #     path = "rd?ep=node1&con=coap://local-proxy-old.example.com:" + str(port) + "&et=oic.d.sensor&account=admin@test&resnbr="+str(resource_number)
    #     ct = {'content_type': defines.Content_types["application/link-format"]}
    #     payload = '</sensors/temp>;ct=41;rt="temperature-c";if="' + if_name + '";anchor="coap://spurious.example.com:' + str(
    #         port) + '",' \
    #                 '</sensors/light>;ct=41;rt="light-lux";if="' + if_name + '"'
    #     response = client.post(path, payload, None, None, **ct)
    #     if (response):
    #         location_path = response.location_path
    #         print(response.pretty_print())
    #     else:
    #         print('no response')
    #     client.stop()
    # for x in range(5):
    #     ifs = ['sensor', 'actuator', 'trigger', 'device']
    #     if_name = random.choice(ifs)
    #     path = "rd?ep=node1&con=coap://local-proxy-old.example.com:"+str(port)+"&et=oic.d.sensor&account=admin@test"
    #     ct = {'content_type': defines.Content_types["application/link-format"]}
    #     payload = '</sensors/temp>;ct=41;rt="temperature-c";if="'+if_name+'";anchor="coap://spurious.example.com:'+str(port)+'",' \
    #               '</sensors/light>;ct=41;rt="light-lux";if="'+if_name+'"'
    #     response = client.post(path, payload, None, None, **ct)
    #     if(response):
    #         location_path = response.location_path
    #         print(response.pretty_print())
    #     else:
    #         print('no response')

    # Resource lookup
    # for x in range(30):
    # rd_number = 6
    # rd_ = random.randint(0, rd_number - 1)
    # port = 5551 + rd_
    port = int(sys.argv[1])
    client = HelperClient(server=(host, port))
    path = 'rd-lookup/res?if=sensor'
    response = client.get(path)
    print(response.pretty_print())
    client.stop()
    #
    # # Update a registration resource
    # path = location_path + "?con=coaps://new.example.com:5684"
    # response = client.post(path, '')
    # print(response.pretty_print())
    #
    # # Read endpoint links
    # path = location_path
    # response = client.get(path)
    # print(response.pretty_print())
    #
    # # Endpoint lookup
    # path = 'rd-lookup/ep?et=oic.d.sensor'
    # response = client.get(path)
    # print(response.pretty_print())
    #
    # # Delete a registration resource
    # path = location_path
    # response = client.delete(path)
    # print(response.pretty_print())

    # client.stop()

if __name__ == '__main__':
    main()