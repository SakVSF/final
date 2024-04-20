#!/usr/bin/env python2
#
# Insert bank server code here.
#
import rpclib
import sys
import bank
from debug import *
import auth_client



def serialise(i):
    return {c.name: getattr(i, c.name) for c in i.__mapper__.columns}

class BankRpcServer(rpclib.RpcServer):
    ## Fill in RPC methods here.

    def rpc_transfer(self,sender, recipient, zoobars, token):
        #ex8 -authentication
        if not auth_client.check_token(sender, token):
            raise ValueError('authentication failed')
        
        
        return bank.transfer(sender, recipient, zoobars)

    def rpc_balance(self, username):
        return bank.balance(username)

    def rpc_get_log(self, username):
        var1 =  bank.get_log(username) #needs to be serialized
        return [serialise(i) for i in var1]

    def rpc_create_zoobars(self, username):
        return bank.create_zoobars(username)

(_, dummy_zookld_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)
