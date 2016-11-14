#!/usr/bin/python

# Script to commit configuration using 'xml' format using PyEZ.
# Author: Satya (dsatya@juniper.net)

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device()
dev.open()
config_xml = """
    <configuration>
        <system>
            <scripts>
                <op>
                    <file>
                        <name>demo.py</name>
                    </file>
                </op>
            </scripts>
        </system>
    </configuration>
"""
cu = Config(dev)
cu.lock()
cu.load(config_xml, format="xml", merge=True)
cu.commit()
cu.unlock()
dev.close()