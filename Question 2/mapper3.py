#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        a1,a2,a3,a4,a5,a6,a7,a8,a9,a10 = data
        print "{0}\t{1}".format(a7.replace("http://www.the-associates.co.uk",""),1)

