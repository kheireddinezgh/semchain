from coapthon.client.helperclient import HelperClient

host = "127.0.0.1"
port = 5690
path = 'rd-lookup/res?if=sensor'
client = HelperClient(server=(host, port))
response = client.get(path)
print(response.pretty_print())
path = "rd?ep=node1&con=coap://local-proxy-old.example.com:" + str(port) + "&et=oic.d.sensor&account=admin@test"
ct = {'content_type': defines.Content_types["application/link-format"]}
payload = '</sensors/temp>;ct=41;rt="temperature-c";if="' + if_name + '";anchor="coap://spurious.example.com:' + str(
    port) + '",' \
            '</sensors/light>;ct=41;rt="light-lux";if="' + if_name + '"'
response = client.post(path, payload, None, None, **ct)
client.stop()