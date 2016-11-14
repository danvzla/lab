#!/usr/bin/python

# Script to run RPC's using PyEZ.
# Author: Satya (dsatya@juniper.net)

from jnpr.junos import Device
from lxml import etree


jdev = Device(host='choc-mx240-a', user='regress', passwd='MaRtInI', port=22)

# Opens a connection with remote device
jdev.open()

# Run rpc
xml_rsp = jdev.rpc.get_software_information()
print etree.tostring(xml_rsp)

# Close the connection
jdev.close()