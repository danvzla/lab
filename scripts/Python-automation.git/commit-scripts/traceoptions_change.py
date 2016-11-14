#!/usr/bin/python

# Script to commit permanent changes.
# Author: Satya (dsatya@juniper.net)

import jcs

count = 0
trace = "trace"
size = "100m"
files = "10"
flag = "all"

while (count < 5):
    change_xml = """<system><scripts><commit>
                    <traceoptions><file><filename>{0}</filename><size>{1}</size><files>{2}</files></file><flag>{3}</flag>
                    </traceoptions></commit>
                    </scripts></system>""".format(trace + str(count), size, files, flag)

    # Commit permanent changes
    jcs.emit_change(change_xml, "change", "xml")
    count = count + 1