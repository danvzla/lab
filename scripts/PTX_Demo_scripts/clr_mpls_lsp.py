#!/usr/bin/env python
from pprint import pprint
from jnpr.junos import Device
import argparse
from jnpr.junos.utils.config import Config
from lxml import etree

def main ():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-i", action="store",
                    help="IP Address")
    parser.add_argument("-u", action="store",
                    help="user")
    parser.add_argument("-p", action="store",
                    help="password")
    parser.add_argument("-l", action="store",
                    help="lsp")

    args = parser.parse_args()

    ip_address = None
    user = None
    password = None
    lsp_name =None

    if args.i:
        ip_address = args.i
    if args.u:
        user = args.u
    if args.p:
        password= args.p
    if args.l:
        lsp_name = args.l
    
    dev = Device(host = ip_address, user = user, password=password)
    dev.open(gather_facts = False)
    #print "LSP Info BEFORE clearing...."
    #get_mpls_lsp_info(dev, lsp_name)
    clr_mpls_lsp_info(dev, lsp_name)
    #clr_mpls_lsp(dev, lsp_name)
    #print "LSP Info AFTER clearing...."
    #get_mpls_lsp_info(dev, lsp_name)
    dev.close()

def clr_mpls_lsp_info(dev,lsp_name):
    if lsp_name:
        xmlNetconfResult = dev.rpc.clear_mpls_lsp_information(name = lsp_name)
    else:
        xmlNetconfResult = dev.rpc.clear_mpls_lsp_information
    if xmlNetconfResult:
        print "SUCCESSFULLY cleared LSP Counters"
    else:
        print "FAILED to clear LSP Counters!!!!!"

def get_mpls_lsp_info(dev,lsp_name):
    xmlNetconfResult = dev.rpc.get_mpls_lsp_information(name = lsp_name)
    print(etree.tostring(xmlNetconfResult, pretty_print=True))
    
def clr_mpls_lsp(dev,lsp_name):
    cu = Config(dev)
    if lsp_name:
	set_commands = "clear mpls lsp optimize name " + lsp_name
    else:
	set_commands = "clear mpls lsp optimize"
    print set_commands
    cu.load( set_commands, format='set' )

if __name__ == "__main__":
    main()
