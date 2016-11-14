#!/usr/bin/env python

# Script to emit warning/error messages from commit script
# Author: Satya (dsatya@juniper.net)

import jcs


def main():
    jcs.emit_warning("Warning message from Python commit script")
    jcs.emit_error("Error message from Python commit script")

if __name__ == '__main__':
    main()