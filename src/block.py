import json
try:
    import requests
except:
    pass


nodes_api = ["http://blackhole.consulting:8888"]

## WARNING - Don't send unencrypted data

def get_info():
    """
    /v1/chain/get_info
    :return:
    """

    req = requests.post("block.blackhole.consulting",8888,"v1/chain/get_info","","") 
        
    return req

def get_block(blocknum):
    """
    https://eosio.github.io/eos/group__eosiorpc.html#v1chaingetblock
    :param block_num_or_id:
    :return:
    """

    path = "/v1/chain/get_block"

    req = requests.post("router.blackhole.consulting",8888,"v1/chain/get_block","Content-type: application/json","{\"block_num_or_id\": \""+str(blocknum)+"\"}")
    
    return req

def get_account(account_name):
    """
    https://eosio.github.io/eos/group__eosiorpc.html#v1chaingetaccount
    :param account_name:
    :return:
        """

    path = "/v1/chain/get_account"

    req = requests.post("block.blackhole.consulting",8888,"v1/chain/get_account","content-type: application/json","{\"account_name\": \""+account_name+"\"}")
    
    return req


def get_code(account_name):
    """
    :param account_name:
    :return:
    """
    path = "/v1/chain/get_code"

    req = requests.post("block.blackhole.consulting",8888,"v1/chain/get_info","content-type: application/json","{\"account_name\": \""+account_name+"\"}")
        
    return req

    

def get_table_rows(scope: str, code: str, table: str, json: bool=True, lower_bound: int=None,
               upper_bound: int=None, limit: int=None):
	"""
	https://eosio.github.io/eos/group__eosiorpc.html#v1chaingetcode
	:param scope:
	:param code:
	:param table:
	:param json:
	:param lower_bound:
	:param upper_bound:
	:param limit:
	:return:
	"""

	path = "/v1/chain/get_table_rows"


	return requests.post(nodes_api[0]+path,9010,"\ncontent-type: application/json",'{"code": "string","table": "string","scope": "string","index_position": "string","key_type": "string","encode_type": "string","lower_bound": "string","upper_bound": "string","limit": 10,"reverse": false,"show_payer": false}')


def push_transaction(ref_block_num: str, ref_block_prefix: str, expiration: str, scope: list,
                 actions: list, signatures: list, authorizations: list):
	"""
	:param ref_block_num:
	:param ref_block_prefix:
	:param expiration: datetime  iosformat
	:param scope:
	:param actions:
	:param signatures:
	:param authorizations:
	:return:
	"""

	path = "/v1/chain/push_transaction"


	return requests.post(nodes_api[0]+path,9010,"\ncontent-type: application/json",'{"signatures": ["string"],"compression": true,"packed_context_free_data": "string","packed_trx": "string"}')



def get_transaction(txid):

	return 0 

def get_acc_tx(acc):

	return 0 

def get_public_keys(self):
	return 0


def get_accounts():

	return 0

def genKeys():

	return 0

def getbalance(code,acc,symbol):
	return 0

def sign_transaction(self, transaction_list: list):
	"""
	:param transaction_list:
	:return:
	"""
	return 0


