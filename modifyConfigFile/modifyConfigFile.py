#!/usr/bin/env python
"""modifyConfigFile.py:  Modify a simple INI format configuration file."""

__author__		=  "Andrew Diamond"
__copyright__		=  "Copyright 2015, Planet Earth"
__license__		=  "GPL"
__version__		=  "1.0"
__email__			= "adiamond1978 at gmail dot com"

from configobj import ConfigObj
import sys, os, os.path
import getopt
import argparse
import shutil

def modifyConfigFile(configFile, section, key, value):
	try:
		config = ConfigObj(configFile)
		config.write_empty_values = True
		config[section][key] = value
		config.write()
	except Exception, msg:
		print('Failed to modify %s -- %s' % (configFile, msg))
		sys.exit(1)

def main(argv):

	parser = argparse.ArgumentParser(description='Modify an INI format configuration file')
	parser.add_argument('-i', '--input', help = 'name of config file to modify', required = True)
	parser.add_argument('-s', '--section', help = 'name of section enclosed in [] to search for key', required = True)
	parser.add_argument('-k', '--key', help = 'name of the key to modify', required = True)
	parser.add_argument('-v', '--value', help = 'new value', required = True)
	args = parser.parse_args()
        
	# Check if file exists, is readable, and writeable.
	# Exit if not.
	if not os.path.isfile(args.input):
		print("Not a file, or file doesn't exist")
        	sys.exit(1)
    	if not os.access(args.input, os.R_OK):
        	print("Cannot read from %s" % args.input)
        	sys.exit(1)
    	if not os.access(args.input, os.W_OK):
        	print("Cannot write %s" % args.input)
        	sys.exit(1)	

	# See if a backup of the original file exists, and create one if it doesn't.
	if not os.path.isfile(args.input + ".bak"):
		try:	
			shutil.copy(args.input, args.input + ".bak")
			print("Created backup file %s" % args.input + ".bak")
		except Exception, msg:
			print("Failed to create backup file %s  -- %s" % (args.input + ".bak", msg))
			sys.exit(1)

        modifyConfigFile(args.input, args.section, args.key, args.value)

if __name__ == "__main__":
    main(sys.argv[1:])
