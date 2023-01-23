import sys

for line in sys.stdin:
    entry = line.strip().split()
    print("{}\t{}".format(entry[3], "-".join((entry[0], entry[1], entry[2]))))
