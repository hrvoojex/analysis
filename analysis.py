#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, argparse


# Read, regex and write a new file
def processMyFile(file):
    rsltList = []
    with open(file, 'r') as fh:
        myList = [line.strip() for line in fh]
    for item in myList:
        x = re.compile(".*SLA. (\d{1,4})")
        if x.findall(item) != []:
            rsltList.append(x.findall(item))
    saveFile = "result" + file[-5:-4] + ".txt"
    with open(saveFile, "w") as fh:
        for subList in rsltList:
            for item in subList:
                if int(item) >= 0 and int(item) <= 100:
                    fh.write(item + "\n")
    print("\"{}\" created successfully.".format(saveFile))


# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="enter a file name")
parser.add_argument("-d", "--directory", help="enter a directory name")
args = vars(parser.parse_args())

# File is entered as a cmd argument
if args["file"] != None and os.path.isfile(args["file"]):
    processMyFile(args["file"])
    os._exit(0)

# Directory is entered as a cmd argument
if args["directory"] != None and os.path.isdir(args["directory"]):
    myDataFiles = []
    os.chdir(args["directory"])
    for myDataFile in os.listdir(args["directory"]):
        if myDataFile.endswith(".txt") and myDataFile.startswith("data"):
            myDataFiles.append(myDataFile)
    for file in myDataFiles:
        processMyFile(file)
        