#DRDChain

This is the code of our paper untitled **DRDChain : A Blockchain-based Distributed Resource
Directory for the Internet of Things**.

Below are the steps for reproducing the framework environment.
(We recommend using Linux Ubuntu OS)

1. Install [Docker](https://docs.docker.com/get-docker/)
2. Deploy [Hyperledger Iroha](https://iroha.readthedocs.io/en/develop/getting_started/index.html)
3. Run Postgres and HL Iroha containers
```
$ sudo docker container start some-postgres
$ sudo docker container start iroha
```
4. Install [MongoDB](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/) for CoAPthon Resource Directory.
5. MongoDB process must be started. Run this command on your terminal :
```
$ mongod
```
6. Following the credentials defined in this file :
```
venv/lib/python3.8/site-packages/coapthon/defines.py
```
Open [MongoDB shell](https://www.mongodb.com/docs/mongodb-shell/) and configure the used databases.
```
> use rd
> db.createUser( {user: "RD",pwd: "res-dir",roles: [ { role: "readWrite", db: "rd" } ] } )
> db.resources.createIndex( { "ep": 1, "d": 1 }, { unique: true } )
```
7. Clone the repository.

`Discovery.sol` and `Registration.sol` are the Smart Contracts used in the framework. [Deploy them in the Blockchain](https://iroha.readthedocs.io/en/develop/develop/api/commands.html#call-engine) using their Bytecodes (generated from [Remix IDE](https://remix.ethereum.org/)) in order to execute their functions.

You can now run multiple Resource Directories in the same machine with different ports using the configurable file `run-multiple-RD.py`.
You can use different machines with different IPs and ports by configuring `rd.py` file. (The RDs must be [added as peers](https://iroha.readthedocs.io/en/develop/develop/api/commands.html#add-peer) in the Blockchain)

You can also run multiple RD clients (or providers) using `run-multiple-clients.py`. You can configure their action, IP and port from `clientRD.py`.

