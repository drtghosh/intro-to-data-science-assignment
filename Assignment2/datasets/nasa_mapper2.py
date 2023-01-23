import sys

for line in sys.stdin:
    entry = line.strip().split('\t')
    print(f"{entry[0]}\t{entry[1]}")
    