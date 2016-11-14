from jnpr.junos import Device

dev = Device(host='172.16.0.2', user='root', password='Juniper', gather_facts=False)
dev.open()

print dev.cli("show version", warning=False)

dev.close()
