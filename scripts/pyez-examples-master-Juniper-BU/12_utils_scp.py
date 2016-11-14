from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP

dev = Device(host='172.16.0.2', user='root', password='Juniper', gather_facts=False)
dev.open()

with SCP(dev, progress=True) as scp:
     scp.get('/var/tmp/daniel.log','info.txt')
dev.close()
