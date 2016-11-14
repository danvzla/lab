from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device(host='172.16.0.2', user='root', password='Juniper', gather_facts=False)
dev.open()

cu = Config(dev)
diff = cu.diff()
if diff:
    cu.rollback()
dev.close()
