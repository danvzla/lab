from jnpr.junos import Device
from lxml import etree

dev = Device(host='172.16.0.2', user='root', password='Juniper', gather_facts=False)
dev.open()

cnf = dev.rpc.get_config()
#cnf = dev.rpc.get_config(filter_xml=etree.XML('<configuration><interfaces/></configuration>'))
print etree.tostring(cnf)
