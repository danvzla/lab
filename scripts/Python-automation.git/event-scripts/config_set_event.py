#!/usr/bin/python

# Script to commit configuration using 'set' format using PyEZ.

# Based on receiving an event configured for an event policy, following
# script will be triggered.

# Author: Satya (dsatya@juniper.net)


from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device()
dev.open()
config_set = """
set routing-options static route 10.3.0.0/16 next-hop 192.168.1.1
set routing-options static route 10.3.0.0/16 next-hop 192.168.1.2
"""
cu = Config(dev)
cu.lock()
cu.load(config_set, format="set", merge=True)
cu.commit()
cu.unlock()
dev.close()