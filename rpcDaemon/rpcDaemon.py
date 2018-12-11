#!/usr/bin/env python
#
# Pablo Munoz (c) 2018
#
# Daemon process with rpc serving capability
#
#
import os
import logging
import zerorpc
from daemons.prefab.run import RunDaemon


class RpcDaemon(RunDaemon):
    def __init__(self):
        super(RunDaemon, self).__init__(pidfile=os.path.join(os.getcwd(), '.rpcd.pid'))

    def target(self, serveObject):
        self.serveObject = serveObject

    def run(self):
        self.serve()

    def serve(self):
        logger = logging.getLogger('log.daemon.serve')
        logger.debug('running serve @pid {}'.format(os.getpid()) )
        self.server = zerorpc.Server(self.serveObject)
        self.server.bind('tcp://0.0.0.0:4242')
        self.server.run()

