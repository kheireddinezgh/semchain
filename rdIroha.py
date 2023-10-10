import binascii
from iroha import Iroha, IrohaGrpc
from iroha import IrohaCrypto as ic
import commons
import os
import sys

# admin = commons.new_user('admin@test')
alice = commons.new_user('alice@test')
# bob = commons.new_user('bob@test')
# iroha = Iroha(admin['id'])

IROHA_HOST_ADDR = os.getenv('IROHA_HOST_ADDR', '127.0.0.1')
IROHA_PORT = os.getenv('IROHA_PORT', '50051')
ADMIN_ACCOUNT_ID = os.getenv('ADMIN_ACCOUNT_ID', 'admin@test')
ADMIN_PRIVATE_KEY = os.getenv(
    'ADMIN_PRIVATE_KEY', 'f101537e319568c765b2cc89698325604991dca57b9716b58016b253506cab70')

iroha = Iroha(ADMIN_ACCOUNT_ID)
net = IrohaGrpc('{}:{}'.format(IROHA_HOST_ADDR, IROHA_PORT))


def trace(func):
    """
    A decorator for tracing methods' begin/end execution points
    """

    def tracer(*args, **kwargs):
        name = func.__name__
        print('\tEntering "{}"'.format(name))
        result = func(*args, **kwargs)
        print('\tLeaving "{}"'.format(name))
        return result

    return tracer


@trace
def send_transaction_and_print_status(transaction):
    global net
    hex_hash = binascii.hexlify(ic.hash(transaction))
    print('Transaction hash = {}, creator = {}'.format(
        hex_hash, transaction.payload.reduced_payload.creator_account_id))
    net.send_tx(transaction)
    for status in net.tx_status_stream(transaction):
        print(status)


class RdIroha:
    def __init__(self, account_name):
        self.account_name = account_name

    # add resource to account detail
    def addResourceToAccountDetail(self, resource):
        # todo : user databaseManager.parseCoreLinkformat function in resource to get Dictionnary
        tx = iroha.transaction([
            iroha.command('SetAccountDetail', account_id=self.account_name, key='resource', value=resource)
        ])
        ic.sign_transaction(tx, ADMIN_PRIVATE_KEY)
        send_transaction_and_print_status(tx)

    def getResourceFromAccountDetail(self, resource):
        query = iroha.query('GetAccountDetail', account_id=self.account_name)
        ic.sign_query(query, ADMIN_PRIVATE_KEY)
        response = net.send_query(query)
        data = response.account_detail_response
        print('Account id = {}, details = {}'.format(self.account_name, data.detail))

    # register a resource in account detail and add an asset quantity
    # def register(self, uri_query, payload, with_smart_contract=False):
    #     if(with_smart_contract):
    #         # using smart contract (EVM)
    #
    #     else:
    #         # using set account detail
    #
    #     return
