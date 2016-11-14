# Script to dump commit script input to a file .
# Author: Satya (dsatya@juniper.net)

from junos import Junos_Configuration


def main():
    root = Junos_Configuration
    # Open a file
    fo = open("/var/tmp/commit_input_extract.txt", "w+")

    for elem in root.iter():
        # Dump the tag
        if elem.tag:
                fo.write(str("        TAG-> "))
                fo.write(str(elem.tag))
        # Dump the element
        if elem.attrib:
                fo.write(str("        ATTRIBUTE-> "))
                fo.write(str(elem.attrib))
        # Dump the text
        if elem.text:
                fo.write(str("        VALUE -> "))
                fo.write(str(elem.text))
        fo.write("\n")
    # Close the file
    fo.close()

if __name__ == '__main__':
    main()