#-----------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# Extract the hostname from a JUNOS configuration file.
#
# CONTACT:   bvilletard@juniper.net; cbinckly@juniper.net; ksator@juniper.net; pgeenens@juniper.net; tgrimonet@juniper.net
#
# CREATED:  2015-11-11
#
# VERSION: 1
#
# USAGE: extract_hostname.py
# -----------------------------------------------------------------------------------------------------------------------
 
# show_config.txt is a JUNOS configuration file
f=open("python_basics/show_config.txt")
for line in f:
	if "host-name" in line:
		hostname=line.split(" ")[-1].strip()
		print hostname
f.close()


