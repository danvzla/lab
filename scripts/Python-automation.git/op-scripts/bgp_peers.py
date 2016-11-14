# Script to identify of active bgp peers.
# Author: Satya (dsatya@juniper.net)

from jnpr.junos import Device

dev = Device()
# Opens a connection
dev.open()

result = dev.rpc.get_bgp_summary_information()
data = result.xpath("//bgp-information")

print "ACTIVE BGP PEERS:"
print "================="
print "IP\t\tASN\tFLAPS\tTIME"

# Loop through bgp peers configuration and identify active peers
for id1 in data:
    for id2 in id1.getiterator(tag='bgp-peer'):
        if id2.find('peer-state').text == 'Active':
            print id2.find('peer-address').text + "\t" + id2.find('peer-as').text
            + "\t" + id2.find('flap-count').text + "\t" + id2.find('elapsed-time').text

# Close the connection
dev.close()