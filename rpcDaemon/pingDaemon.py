#!/usr/bin/env python
import sys
import zerorpc

def getAddress(protocol, host, port):
    return "{}://{}:{}".format(protocol, host, port)

class RpcClient():
    def __init__(self, protocol='tcp', host='0.0.0.0', port='4242'):
        self.client = zerorpc.Client(timeout=30)
        self.client.connect(getAddress(protocol, host, port))

    def submitCommand(self, command, *args, **kwargs):
        return getattr(self.client, command)(*args, **kwargs)

if __name__ == '__main__':
    # Submit command to rpc daemon
    cmdArgs = sys.argv[1:]
    rpcClient = RpcClient()
    result = rpcClient.submitCommand('ping', *cmdArgs)
    print(result)







