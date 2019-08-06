#!/usr/bin/env python

#author: Sabrina Speranza
#this code implements what is done in the CKB ontology in order to switch from the extroverted personality to the introverted one and vice versa
#this implementation is based on a previous study: "Taking care of the linguistic feature of extraversion"

import nltk #NLTK tool --> http://www.nltk.org/book/
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from open_file import open_file_function
from functions import extro_intro_switch
from copy_lines import copy_lines

filename = 'topic0.txt'
#filename = 'topic12.txt'
#filename = "topic35.txt"
#filename = "topic38.txt"
#filename = 'topic802.txt'
#filename = "topic1301.txt"
#filename = "topic1314.txt"
##filename = "topic1349.txt"
#filename = "topic1779.txt"
#filename = "topic1791.txt"
#filename = "topic2436.txt"
#filename = "topic2439.txt"
#filename = "topic2902.txt"


#filename = "topic2440.txt"

lineList = open_file_function(filename) #open the file and put sentences in a list

copy_lines(filename, "myOutFile_extro.txt")
copy_lines(filename, "myOutFile_intro.txt")

num_lines = sum(1 for line in open(filename)) - 5 #count the number of sentences in the outF_extro

extro_intro_switch(lineList)

num_lines_extro =  sum(1 for line in open("myOutFile_extro.txt")) -5
num_lines_intro =  sum(1 for line in open("myOutFile_intro.txt")) -5
num_lines_out = num_lines_extro + num_lines_intro

percentage = (num_lines_out * 100)/num_lines # % of sentences switched

print 'NUMBER OF SENTENCES: ', num_lines
print 'NUMBER OF SENTENCES TRANSLATED: ', num_lines_out
print 'PERCENTAGE sentences translated', percentage, '%'
