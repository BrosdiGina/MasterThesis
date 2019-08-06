#!/usr/bin/env python
#import os

def copy_lines(file_input, file_output):
    with open(file_input) as f_inp:
        with open(file_output, "w") as f_out:
            for lines in range(5):
                f_out.write(f_inp.readline().strip()) #copy the first 4 lines in the new text file 
                f_out.write("\n")
