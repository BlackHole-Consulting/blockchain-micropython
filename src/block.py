import json
try:
    import requests
except:
    pass


import json

from ufastecdsa import curve, ecdsa, keys, util

def genkeys():
    private_key, public_key = keys.gen_keypair(curve.P256)
    #print("private_key:", private_key)
    #print("public_key:", public_key.x, public_key.y, public_key.curve.name)
    
    return (private_key,public_key.x,public_key.y,public_key.curve.name)

def sign(message,private_key):
    r, s = ecdsa.sign(message, private_key)
    #print("R:", r)
    #print("S:", s)
    return (r,s)

def verify(message,r,s,publick_key):
    verified = ecdsa.verify((r, s), message, public_key)
    #print(verified)
    return (verified)


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

    req = requests.post("block.blackhole.consulting",8888,"v1/chain/get_block","Content-type: application/json","{\"block_num_or_id\": \""+str(blocknum)+"\"}")
    
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


def get_balance(account_name,symbol):
    """
    https://eosio.github.io/eos/group__eosiorpc.html#v1chaingetaccount
    :param account_name:
    :return:
        """

    path = "v1/chain/get_currency_balance"

    req = requests.post("block.blackhole.consulting",8888,path,"content-type: application/json","{\"code\":\"eosio.token\",\"account_name\": \""+account_name+"\",\"symbol\":\""+symbol+"\" }")
    
    return req

def get_transaction(txid):
    """
    https://eosio.github.io/eos/group__eosiorpc.html#v1chaingetaccount
    :param account_name:
    :return:
        """

    path = "v1/history/get_transaction"

    req = requests.post("block.blackhole.consulting",8888,path,"content-type: application/json","{\"blockNumHint\":null,\"id\": \""+txid+"\" }")

    return req



def get_actions(account_name,pos,offset):
    """
    https://eosio.github.io/eos/group__eosiorpc.html#v1chaingetaccount
    :param account_name:
    :return:
        """

    path = "v1/history/get_actions"

    req = requests.post("block.blackhole.consulting",8888,path,"content-type: application/json","{\"pos\":"+pos+",\"account_name\": \""+account_name+"\",\"offset\":"+offset+" }")

    return req



def get_code(account_name):
    """
    :param account_name:
    :return:
    """
    path = "/v1/chain/get_code"

    req = requests.post("block.blackhole.consulting",8888,"v1/chain/get_info","content-type: application/json","{\"account_name\": \""+account_name+"\"}")
        
    return req

    

def get_table_rows(code,table,scope):

    """
    https://eosio.github.io/eos/group__eosiorpc.html#v1chaingetaccount
    :param account_name:
    :return:
        """

    path = "/v1/chain/get_table_rows"

    req = requests.post("block.blackhole.consulting",8888,"v1/chain/get_account","content-type: application/json","{\"code\":\""+code+"\",\"table\": \""+table+"\",\"scope\":\""+scope+"\"}")
    
    return req



def send_transaction(fro, to,amount, symbol, memo, privkey):

    ## TODO convert from EOS
    path = "v1/chain/send_transaction"
    trx = { "account": "eosio.token",  "name": "transfer",  "authorization": [{"actor": "eosio", "permission": "active"}], "data": {"from": fro,"to": to, "quantity": amount+" "+symbol,"memo": memo}}


    r,v = sign(trx,privkey)
    
    return requests.post("block.blackhole.consulting",8888,"\ncontent-type: application/json",'{"signatures": ["'+r+'","'+v+'"],"compression": true,"packed_context_free_data": "'+memo+'","packed_trx": '+json.dumps(trx)+'}')




