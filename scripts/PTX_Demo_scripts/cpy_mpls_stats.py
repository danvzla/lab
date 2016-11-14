#!/usr/bin/env python
from pprint import pprint
from jnpr.junos import Device
import argparse
from jnpr.junos.utils.scp import SCP
from jnpr.junos.utils.fs import FS
from lxml import etree

def main ():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-i", action="store",
                    help="IP Address")
    parser.add_argument("-u", action="store",
                    help="user")
    parser.add_argument("-p", action="store",
                    help="password")

    args = parser.parse_args()

    ip_address = None
    user = None
    password = None

    if args.i:
        ip_address = args.i
    if args.u:
        user = args.u
    if args.p:
        password= args.p
    
    dev = Device(host = ip_address, user = user, password=password)
    dev.open(gather_facts = False)
    fs = FS(dev)
    myfiles = fs.ls('/var/log').get('files')
    for key in myfiles:
        if key.startswith('mplsstats'):
             with SCP(dev, progress=True) as scp:
                 scp.get("/var/log/%s" % key)
    dev.close()

if __name__ == "__main__":
    main()
