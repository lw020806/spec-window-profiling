import matplotlib.pyplot as plt
import seaborn as sns
import sys
from collections import Counter

fileName = sys.argv[1]

# (br1, dst, br2) ->
#			P -> [c0, c1, c2, ...]
#			M -> [c0, c1, c2, ...]
# (br1, dst, br2) ->
#			P -> [c0, c1, c2, ...]
#			M -> [c0, c1, c2, ...]

datas = {}

with open(fileName, 'r') as inFile:
    for line in inFile:
        line = line.strip().split()
        if line[0] == "#":
            continue
        if len(line) != 6 :
            continue
        predicted = line[1]
        br1 = line[2]
        dst = line[3]
        br2 = line[4]
        cycle = line[5]
        key = (br1, dst, br2)
        if key in datas.keys() :
            datas[key][predicted].append(int(cycle))
        else :
            datas[key] = {"P":[], "M":[]}
            datas[key][predicted].append(int(cycle))

def process(cycles, N, which) :
    if len(cycles) == 0 :
        return [], []
    for i in range(len(cycles)) :
        cycles[i] = cycles[i] # - cycles[i]%N + N/2
    data = Counter(cycles)
    x = []
    y = []                  # _cycle, max = data.most_common(1)[0]
    for cycle, cnt in data.most_common() :
        if cnt > 0 :
            x.append(cycle)
            y.append(cnt/len(cycles))
    return x, y
        
for key in datas.keys() :
    mCycles = datas[key]["M"]
    pCycles = datas[key]["P"]

    if not (len(mCycles) or len(pCycles)) :
        continue

    mx, my = process(mCycles, 1, 0)
    px, py = process(pCycles, 1, 1)

    plt.scatter(mx, my, marker='.', color="red", alpha=0.7, label="Mis: " + str(len(mCycles)))
    plt.scatter(px, py, marker='.', color="blue", alpha=0.7, label="Pred: " + str(len(pCycles)))
    # a = sns.displot(mCycles, kind='kde', color="red")
    # b = sns.displot(pCycles, kind='kde', color="blue").label("Pred: " + str(len(pCycles)))

    plt.xlim((0, 100))
    tp = key[0] + "-" + key[1] + "-" + key[2]
    plt.title(tp)
    plt.legend()
    plt.savefig(tp + ".png", dpi=400)
    plt.close()

