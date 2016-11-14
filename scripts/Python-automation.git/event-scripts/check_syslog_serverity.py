#!/usr/bin/env python

# Script to log syslog severity for an triggered event of a configured event policy
# Author: Satya (dsatya@juniper.net)
# How to trigger ?
#   $: logger -e DUMMY_EVENT "This is sample message"
# Sample output:
#   $: Jan 20 05:31:37  choc-mx480-a cscript: logger[57854]: This is sample message
# Sample configuration:
#  $# show event-options
#      policy DUMMY {
#          events DUMMY_EVENT;
#      then {
#          event-script check_syslog_severity.py;
#      }
#  }
#  event-script {
#      file check_syslog_severity.py;
#  }
#


from junos import Junos_Trigger_Event
import jcs


def main():
    # Record the facility
    facility = str(Junos_Trigger_Event.xpath('//trigger-event/facility')[0].text)
    # Get the process name
    process_name = str(Junos_Trigger_Event.xpath('//trigger-event/process/name')[0].text)
    # Get PID
    pid = str(Junos_Trigger_Event.xpath('//trigger-event/process/pid')[0].text)
    # Get the syslog message
    message = str(Junos_Trigger_Event.xpath('//trigger-event/message')[0].text)

    # Assemble message
    if int(pid) > 0:
        final_message = process_name + "[" + pid + "]: " + message
    else:
        final_message = process_name + ": " + message

    # New Priority
    new_priority = facility + ".notice"

    # Now re-syslog it with the new facility
    jcs.syslog(new_priority, final_message)

if __name__ == '__main__':
    main()