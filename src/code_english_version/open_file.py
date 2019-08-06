#!/usr/bin/env python

def open_file_function(filename):
    with open(filename) as fp:
        for cnt, line in enumerate(fp):
            lineList = [line.rstrip('\n') for line in open(filename)] #create the list of sentences
    return lineList
