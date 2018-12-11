#!/usr/bin/env python
#
# Pablo Munoz (c) 2018
#
# Daemon client abstraction
#
import zerorpc


class RpcClient():
    def __init__(self, protocol='tcp', host='0.0.0.0', port='4242'):
        self.client = zerorpc.Client(timeout=30)
        self.client.connect(getAddress(protocol, host, port))

    def submitCommand(self, command, *args, **kwargs):
        return getattr(self.client, command)(*args, **kwargs)

def getAddress(protocol, host, port):
    return "{}://{}:{}".format(protocol, host, port)
