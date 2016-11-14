from jnpr.junos.utils.fs import FS
from jnpr.junos import Device
from pprint import pprint

dev = Device(host='172.16.0.2', user='root', password='Juniper', gather_facts=False)
dev.open()

fs = FS(dev)
pprint(fs.ls('/var/tmp'))

dev.close()
