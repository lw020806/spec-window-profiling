import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import sys
import glob
import re
import matplotlib.cm as cm
import numpy as np
import pprint
import collections


inputFileName = sys.argv[1]
PC = sys.argv[2]
cnt = sys.argv[3]

output_file = "first-filter-"+str(PC)+".txt"

with open(inputFileName, "r") as file_in:
    with open(output_file, 'w') as out:
        out.write("# Target PC: " + str(PC) + "freq: "+ str(cnt))
        out.write("# prevCycle\tP/M\tbranch1\tdestination\tbranch2\tthisCycle\n")
        for line in file_in:
            line = line.strip().split()
            if len(line) == 0 or len(line) == 1:
                continue

            i = len(line) - 1
            matter = False
            while i > 0 :
                curRecord = line[i].split("/")
                if len(curRecord) != 6 :
                    continue
                curBr = curRecord[0]
                curDst = curRecord[1]
                curP = curRecord[2]
                curCycle = curRecord[5]
                if matter :
                    out.write(curBr + "\t" + curCycle + "\n")
                    matter = False
                if curBr == PC :
                    matter = True
                    out.write(curCycle + "\t" + curP + "\t" + curBr + "\t" + curDst + "\t")
                i = i - 1
            if matter :
                out.write("\n")


            
