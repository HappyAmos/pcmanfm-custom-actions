#!/usr/bin/env python
"""findAndReplace.py:  Find and replace a string in a text file"""

__author__		=  "Andrew Diamond"
__copyright__		=  "Copyright 2015, Planet Earth"
__license__		=  "GPL"
__version__		=  "1.0"
__email__		= "adiamond1978 at gmail dot com"

import sys, os, os.path
import argparse

def isYesQuery(question, defaultAnswer = ""):
    """ Ask the user a Y/N question on the command line.  If the user doesn't
        give the correct answer, then it asks again.
        :param question A string that contains the question you'd like
        to ask the user
        :param defaultAnswer If set, the prompt defaults to this answer when
        the user presses enter/return.  Valid defaults are yes, y, true, t
        no, n, false, f. If no default is given, then the user must explicity
        enter a (y)es or (n)o answer.
    """
    yes = set(['yes','y', "t", "true"])
    no = set(['no','n', "f", "false"])

    defaultAnswer = defaultAnswer.lower()

    if defaultAnswer in yes:
        prompt = "[Y/n]"
        yes.add("")
    elif defaultAnswer in no:
        prompt = "[y/N]"
        no.add("")
    elif defaultAnswer == "":
        prompt = "[y/n]"
    else:
        # The programmer didn't give a valid defaultAnswer, so raise
        # an exception
        raise ValueError("invalid defaultAnswer: '%s'" % defaultAnswer)

    print(question + " " + prompt)

    while True:
        choice = raw_input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print("Please respond with " + prompt)

def main():
    # https://docs.python.org/2/howto/argparse.html
    parser = argparse.ArgumentParser(description='Find and replace a string in a text file')
    parser.add_argument('-i','--input', help='Input file name',required=True)
    parser.add_argument('-f','--find',help='Text string to search for. Enclose in quotes and escape if required', required=True)
    parser.add_argument('-r','--replace',help='Text string to replace searched text for. Enclose in quotes and escape if required', required=False)
    parser.add_argument('-c','--confirm', help='Confirm each replace',required=False, action="store_true")
    parser.add_argument('-v','--verbose', help='Verbose output',required=False, action="store_true")
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
    
    
    try:
        linesChanged = 0
        newText = ""
        tempFile = args.input + ".bak"
        f1 = open(args.input, 'r')
        if args.verbose:
            print "Creating %s" % tempFile
        f2 = open(tempFile, 'w')
        if args.replace:
            newText = args.replace

        for line in f1:
            #temp = line
            #temp2 = line
            if args.confirm and args.find in line:
                temp = temp.replace(args.find, newText)
                try:
                    question = "Replace: [%s]\nwith: [%s]" % (line.rstrip('\n'), line.replace(args.find, newText).rstrip('\n'))
                    if isYesQuery(question, "yes"):
                        f2.write(line.replace(args.find, newText))
                        # Keep track of the number of changes we make.
                        linesChanged += 1
                        if args.verbose:
                            print "Changed: " + line.rstrip('\n') + " => " + line.replace(args.find, newText).rstrip('\n')
                    else:
                        f2.write(line)
                        if args.verbose:
                            print "Unchanged: " + line.rstrip('\n')
                except Exception, arg:
                    print("Error: ", arg)
            elif not args.confirm and args.find in line:
                f2.write(line.replace(args.find, newText))
                # Keep track of the number of changes we make.
                linesChanged += 1
                if args.verbose:
                    print "Changed: " + line.rstrip('\n') + "=>" + line.replace(args.find, newText).rstrip('\n')
            else:
                f2.write(line)
                if args.verbose:
                    print "Unchanged: " + line.rstrip('\n')

        # Close our open files
        f1.close()
        f2.close()

        if args.verbose:
            print "Removing %s file..." % args.input
        # Delete the original file
        os.remove(args.input)
        if args.verbose:
            print "Done removing %s" % args.input
        if args.verbose:
            print "Renaming %s to %s" % (tempFile, args.input)
        # Rename the temp file to our original file.
        os.rename(tempFile, args.input)
        if args.verbose:
            print "Done. %s lines modified." % linesChanged
    except IOError:
        print("Could not read or write to %s" % args.input)
        sys.exit(1)
    

if __name__ == "__main__":
    main()
