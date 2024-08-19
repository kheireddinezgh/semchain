from coapthon.client.helperclient import HelperClient

host = "127.0.0.1"
port = 5690
path = 'rd-lookup/res?if=sensor'
client = HelperClient(server=(host, port))
response = client.get(path)
print(response.pretty_print())
client.stop()