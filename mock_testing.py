import time
from constants import CONSTANT_VAL

class Calculator:
    def sum(a, b):
        return a + b

def api_call():
    time.sleep(120)
    return("Call completed!")

def slowAPI():
    return api_call()

def returnVal():
    # time.sleep(1000)
    # RETURN_VAL = valCalc() 
    RETURN_VAL = CONSTANT_VAL
    return RETURN_VAL
