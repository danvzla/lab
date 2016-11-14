from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import yaml

dev = Device(host='172.16.0.2', user='root', password='Juniper', gather_facts=False)
dev.open()

data = yaml.load(open('protocol_data.yml'))

cu = Config(dev)

cu.load(template_path='protocol_temp.j2', template_vars=data, format='text')
cu.pdiff()
if cu.commit_check():
   cu.commit()
else:
   cu.rollback()

dev.close()
