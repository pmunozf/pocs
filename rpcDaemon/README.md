 Testing python daemons with rpc capabilities

rpcDaemon $ ./launchDaemon.py
    This script launches a python daemon that serves a test python object on a tpc
    channel run by zerorpc. By default it stores a pidfile with the pid of the daemon
    on ../rpcDaemon/.rpcd.pidfil and binds the server to tcp://0.0.0.0:4242

rpcDaemon $ ./killDaemon.py
    Kills the spawned daemon process

rpcDaemon $ ./pingDaemon.py MSG1 MSG2 ...
    Connects to the daemon and submits a command to the served object through a zerorpc client

