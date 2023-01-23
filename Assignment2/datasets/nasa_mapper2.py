import sys

for line in sys.stdin:
    entry = line.strip().split('\t')
    print("{}\t{}".format(entry[0], entry[1]))
