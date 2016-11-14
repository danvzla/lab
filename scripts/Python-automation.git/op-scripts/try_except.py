# Script to catch exception, if user enters non integer value.
# Author: Satya(dsatya@juniper.net)

while True:
    try:
        n = raw_input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")

print "Entered valid integer!"