#!/usr/bin/python
import sys
Total = 0
oldKey = None
finalKey=None
finalCount=0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    Key,Value = data_mapped

    if oldKey and oldKey != Key:
       # print oldKey, "\t",Total
       # oldKey = Key;
	if finalCount<Total:        
	    finalCount=Total
	    finalKey=oldKey
	Total = 0
	oldKey=Key 

    oldKey = Key
    Total += float(Value)

if oldKey != None:
    print finalKey, "\t",finalCount

