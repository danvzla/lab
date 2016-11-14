#!/usr/bin/env python

# This script pings the configured "host" and prints the rtt details. The number of attempts for averaging is also configured in "count".
#
# This op-script can be called from timer based event-policy to continuously ping the remote host and log the rtt details.
#
# This script is a Python transcription of op-ping-rtt.slax.

# Author: Ali Zaringhalam (azaringhalam@juniper.net)

"""
Example configuration for averaging 5 attempts every 60 seconds:
admin@chicago# show event-options generate-event EVERY_MIN 
time-interval 60;
admin@chicago# show event-options policy ping-rtt
events EVERY_MIN;
then {
    event-script ping-rtt.py {
        arguments {
            host 10.10.10.10;
            count 5;
        }
    }
}
admin@chicago# show event-options event-script
file ping-rtt.py;
Sample output:
messages:Feb 17 18:11:38  chicago cscript: Rtt details for host 10.10.10.10 at time Tue Feb 17 18:11:31 2015 Minimum = 1002 Maximum = 1082 Average = 1042
"""

import argparse
import jcs
from jnpr.junos import Device
from junos import Junos_Context

def main():
	parser = argparse.ArgumentParser(description='Pings remote host and prints the rtt details.')
	parser.add_argument('-host', required=True, help='IP address of remote host')
	parser.add_argument('-count', required=True, help='Number of attempts')

	args = parser.parse_args()

	# infra passes arguments in "".  Strip them.
	args.host = args.host[1:-1]
	args.count = args.count[1:-1]


	dev = Device()
	dev.open()  

        try:
		result = dev.rpc.ping(host=args.host, count=args.count)
                message = "Rtt details for host " + result.findtext("target-host").lstrip().rstrip() + " at time " + str(Junos_Context['localtime']) \
                        + " Minimum = " + result.findtext("probe-results-summary/rtt-minimum").lstrip().rstrip()    \
                        + " Maximum = " + result.findtext("probe-results-summary/rtt-maximum").lstrip().rstrip()    \
                        + " Average = " + result.findtext("probe-results-summary/rtt-average").lstrip().rstrip()
        except:
                message = "Ping to host " + str(args.host) + " at time " + str(Junos_Context['localtime']) + " failed"

	jcs.syslog("external.info", message)

        dev.close()


if __name__ == '__main__':
	main()