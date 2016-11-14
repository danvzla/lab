Step One:
Connect to and find out the rpc for the command
  ssh root@172.16.0.2 
cli
  show interfaces terse | display xml rpc

Verify Its XML output
  show interfaces terse | display xml

Step Two:
Connect via Netconf
  ssh root@172.16.0.2 -s netconf
Issue the Rcp
  <rpc><get-interface-information><terse/></get-interface-information></rpc>
Verify the XML Output and Disconnect
ctl-d
