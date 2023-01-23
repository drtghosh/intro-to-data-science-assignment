import sys

for line in sys.stdin:
    entry = line.strip().split('\t')
    print(f"({entry[3]}\t{','.join(entry[0], entry[1], entry[2])})")
