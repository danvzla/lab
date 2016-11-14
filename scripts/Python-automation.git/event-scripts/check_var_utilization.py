# Script to check for '/var' utilization and log a message to syslog
# Author : Satya (dsatya@juniper.net)

from jnpr.junos import Device
import jcs


def main():
    jdev = Device()

    # Opens a connection
    jdev.open()

    # Get show system storage
    rsp = jdev.rpc.get_system_storage()
    # rsp = jdev.cli("show system storage", format="xml")

    # Retrieve the '/var' percent
    percent = rsp.xpath(".//filesystem[normalize-space(mounted-on)='/var']/used-percent")[0].text
    strip_percent = int(percent.strip())

    if strip_percent > 75:
        syslog_message = "Warning: /var utilization is at " + str(strip_percent) + "%"
        jcs.syslog("external.warning", syslog_message)

    # Close the connection
    jdev.close()

if __name__ == '__main__':
    main()