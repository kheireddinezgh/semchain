#SemChain

This is the code of our paper untitled **SemChain : A Blockchain-based Semantic discovery on Distributed Resource Directories for the Internet of Things**.

Below are the steps for reproducing the framework environment.
(We recommend using Linux Ubuntu OS)

1. Install [Docker](https://docs.docker.com/get-docker/)
2. Deploy [Hyperledger Iroha](https://iroha.readthedocs.io/en/develop/getting_started/index.html)
3. Run Postgres and HL Iroha containers
```
$ sudo docker container start some-postgres
$ sudo docker container start iroha
```
4. Install [Fuseki Server](https://jena.apache.org/download/index.cgi) to manage RDF instances.
5. Enter Fuseki directory and run the server (Java17 is required) :
```
$ ./fuseki-server
```
6. Create a dataset using Fuseki UI through this link  :
```
http://localhost:3030/
```
7. Define SEMANTIC_DATASET with the used name in previous step in this file :
```
venv/lib/python3.8/site-packages/coapthon/defines.py
```

8. Clone the repository.

`Discovery.sol` and `Registration.sol` are the Smart Contracts used in the framework. [Deploy them in the Blockchain](https://iroha.readthedocs.io/en/develop/develop/api/commands.html#call-engine) using their Bytecodes (generated from [Remix IDE](https://remix.ethereum.org/)) in order to execute their functions.

You can now run multiple Resource Directories in the same machine with different ports using the configurable file `run-multiple-RD.py`.
You can use different machines with different IPs and ports by configuring `rd.py` file. (The RDs must be [added as peers](https://iroha.readthedocs.io/en/develop/develop/api/commands.html#add-peer) in the Blockchain)

You can also run multiple RD clients (or providers) using `run-multiple-clients.py`. You can configure their action, IP and port from `clientRD.py`.

