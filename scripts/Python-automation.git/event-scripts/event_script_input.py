#!/usr/bin/env python

# Script to dump few event script input details to a file.
# Author: Satya (dsatya@juniper.net)

from junos import Junos_Context
from junos import Junos_Trigger_Event


def main():
    fo = open("/var/tmp/event_input_extract.txt", "w+")
    fo.write("Event script input: \n")
    fo.write("******************* \n")
    fo.write("Junos context info: \n")
    fo.write("******************* \n")
    fo.write(str(Junos_Context))

    fo.write("\n\nTriggering event details: \n")
    fo.write("*************************\n")
    fo.write("id: " + str(Junos_Trigger_Event.xpath('//trigger-event/id')[0].text) + "\n")
    fo.write("type: " + str(Junos_Trigger_Event.xpath('//trigger-event/type')[0].text) + "\n")
    fo.write("generation-time: " + str(Junos_Trigger_Event.xpath('//trigger-event/generation-time')[0].text) + "\n")
    fo.write("process-name: " + str(Junos_Trigger_Event.xpath('//trigger-event/process/name')[0].text) + "\n")
    fo.write("process-pid: " + str(Junos_Trigger_Event.xpath('//trigger-event/process/pid')[0].text) + "\n")
    fo.write("hostname: " + str(Junos_Trigger_Event.xpath('//trigger-event/hostname')[0].text) + "\n")
    fo.write("facility: " + str(Junos_Trigger_Event.xpath('//trigger-event/facility')[0].text) + "\n")
    fo.write("severity: " + str(Junos_Trigger_Event.xpath('//trigger-event/severity')[0].text) + "\n")
    fo.close()

if __name__ == '__main__':
    main()