#!/usr/bin/env python
"""modifyConfigFile.py:  Modify a simple INI format configuration file."""

__author__		=  "Andrew Diamond"
__copyright__		=  "Copyright 2015, Planet Earth"
__license__		=  "GPL"
__version__		=  "1.0"
__email__			= "adiamond1978 at gmail dot com"

from configobj import ConfigObj
import sys, getopt

def modifyConfigFile(configFile, section, key, value):
    config = ConfigObj(configFile)
    #config.filename = configFile
    config.write_empty_values = True

    #config[section] = {}
    config[section][key] = value

    config.write()

def main(argv):
    reqArgs = {"i" : False, "s" : False, "k" : False, "v" : False}
    helpText = """
Usage: modifyConfigFile.py -i <inputfile> -s <section> -k <key> -v <value>

    --help, -h
        print usage summary
    --ifile, -i
        input file, name of config file to modify
    --section, -s
        name of section enclosed in [] to search for key
    --key, -k
        name of the key to change value for
    --value, -v
        replacement value for this key

"""

    if (len(sys.argv) < 8):
        print(helpText)
        sys.exit(2)
        
    try:
        opts, args = getopt.getopt(argv, "hi:s:k:v:", ["ifile=", "section=", "key=", "value="])
    except getopt.GetoptError:
        print(helpText)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print(helpText)
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
            reqArgs["i"] = True
        elif opt in ("-s", "--section"):
            section = arg
            reqArgs["s"] = True
        elif opt in ("-k", "--key"):
            key = arg
            reqArgs["k"] = True
        elif opt in ("-v", "--value"):
            value = arg
            reqArgs["v"] = True
    if (reqArgs["i"] == True and reqArgs["s"] == True and reqArgs["k"] == True and reqArgs["v"] == True):    
        modifyConfigFile(inputFile, section, key, value)
    else:
        print(helpText)
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])
