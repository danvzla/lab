from pprint import pprint
from jnpr.junos import Device

dev = Device(host='172.16.0.2', user='root', password='Juniper' )
dev.open()

pprint( dev.facts )

dev.close()
