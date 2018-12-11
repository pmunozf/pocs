#!/usr/bin/env python
#
# Pablo Munoz (c) 2018
#
# Daemon process with rpc serving capability
#
import os
import logging
import zerorpc
from daemons.prefab.run import RunDaemon


class RpcDaemon(RunDaemon):
    '''Daemon with rpc facility.'''


    def __init__(self, target=None):
        super(RunDaemon, self).__init__(pidfile=os.path.join(os.getcwd(), '.rpcd.pid'))
        if target:
            self.setTarget(target)
        self.logger = logging.getLogger('log.daemon.serve')

    def setTarget(self, target):
        self.target = target

    def getTarget(self):
        return self.target

    def run(self):
        self.serve()

    def log(self, mode, msg):
        getattr(self.logger, mode)(msg)

    def serve(self):
        self.log('debug', 'running serve @pid {}'.format(os.getpid()))
        self.server = zerorpc.Server(self.getTarget())
        self.server.bind('tcp://0.0.0.0:4242')
        self.server.run()

