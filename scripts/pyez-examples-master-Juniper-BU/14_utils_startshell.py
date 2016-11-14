from jnpr.junos.utils.start_shell import StartShell
from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP

dev = Device(host='172.16.0.2', user='root', password='Juniper', gather_facts=False)
dev.open()

ss = StartShell(dev)
ss.open()
ss.run('cli -c "request support information | save /var/tmp/information.txt"')
with SCP(dev) as scp:
    scp.get('/var/tmp/information.txt','info.txt')
    
ss.close()
