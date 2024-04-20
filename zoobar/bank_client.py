from debug import *
from zoodb import *
import rpclib


# ex7

def transfer(sender, recipient, zoobars, token):
    ## Fill in code here.
    with rpclib.client_connect('/banksvc/sock') as c:
        return c.call('transfer', sender=sender, recipient=recipient, zoobars=zoobars, token=token)


def balance(username):
    ## Fill in code here.
    with rpclib.client_connect('/banksvc/sock') as c:
        return c.call('balance', username=username)

def get_log(username):
    ## Fill in code here.
    with rpclib.client_connect('/banksvc/sock') as c:
        return c.call('get_log', username=username)

def create_zoobars(username):
    ## Fill in code here.
    with rpclib.client_connect('/banksvc/sock') as c:
        return c.call('create_zoobars', username=username)

