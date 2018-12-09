#!/usr/bin/env python
#
# Pablo Munoz (c) 2018
#
# Example use script for python logging facilities
#
#
import logging
FORMAT = 'level: %(levelname)s thread:%(threadName)s module: %(module)s %(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(filename='example.log', level=logging.DEBUG, format=FORMAT)

# Default logging keys
#formats = {
#        'asctime' : '%(asctime)s',
#        'created' : '%(created)f',
#        'filename' : '%(filename)s',
#        'funcname' : '%(funcname)s',
#        'levelname' : '%(levelname)s',
#        'levelno' : '%(levelno)s',
#        'lineno' : '%(lineno)s',
#        'message' : '%(message)s',
#        'module' : '%(module)s',
#        'msecs' : '%(msecs)d',
#        'name' : '%(name)s',
#        'pathname' : '%(pathname)s',
#        'process' : '%(process)d',
#        'processName' : '%(processName)s',
#        'relativeCreated' : '%(relativeCreated)d',
#        'thread' : '%(thread)d',
#        'threadName' : '%(threadName)s'
#
#        }

if __name__ == '__main__':
    d = {'clientip' : '192.168.0.1', 'user': 'pmunoz'}
    logger = logging.getLogger('mylogger')
    logger.debug('Protocol problem: %s', 'connection reset', extra=d)
    logger.info('Protocol problem: %s', 'connection reset', extra=d)
    logger.warning('Protocol problem: %s', 'connection reset', extra=d)
