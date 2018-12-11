#!/usr/bin/env python
#
# Pablo Munoz (c) 2018
#
# Test object to be served on daemon rpc
#
import logging
import os


class TestObject():
    def ping(self):
        logger = logging.getLogger('log.serveObject.ping')
        info = 'Received ping submit'
        logger.debug(info)
        return 'alive @ pid {}'.format(os.getpid())
