from jnpr.junos import Device
from pprint import pprint

dev = Device(host='172.16.0.2', user='root', password='Juniper')
dev.open()

pprint (dev.facts)
