from debug import *
from zoodb import *
import rpclib

def login(username, password):
    ## Fill in code here.
    c = rpclib.client_connect("/authsvc/sock")
    return c.call('login', username=username, password = password)

def register(username, password):
    ## Fill in code here.
    c = rpclib.client_connect("/authsvc/sock")
    return c.call('register', username=username, password=password)


def check_token(username, token):
    ## Fill in code here.
    c = rpclib.client_connect("/authsvc/sock")
    return c.call('check_token' , username=username, token=token)


