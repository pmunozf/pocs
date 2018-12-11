#!/usr/bin/env python
#
# Pablo Munoz (c) 2018
#
# Testing a daemon process with rpc object serving
#
#
import os
import logging
from rpcDaemon import RpcDaemon

class ServeObject():
    def ping(self, *x):
        logger = logging.getLogger('log.serveObject.ping')
        info = 'Received msg: ' + str(x)
        logger.debug(info)
        return 'return:: ' + info

if __name__ == '__main__':
    logging.basicConfig(filename='log', filemode='w', level=logging.DEBUG)
    daemon = RpcDaemon()
    daemon.target(ServeObject())
    print('launching daemon')
    daemon.start()

