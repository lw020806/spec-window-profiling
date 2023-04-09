from collections import Counter
import sys

inFileName = sys.argv[1]

def addDict(d, k, n):
    if k in d.keys() :
        d[k] += n
    else :
        d[k] = n

data = {}
with open(inFileName, 'r') as inFile :
    for line in inFile :
        line = line.strip().split()
        for i in range(1, len(line)) :
            record = line[i].split("/")
            if record[0][2:4] != "40" :
                continue
            addDict(data, record[0], 1)

data = Counter(data)
for pc, cnt in data.most_common() :
    if cnt < 100 :
        break
    print(pc, cnt)
