from pathlib import Path
from collections import defaultdict
import csv

def read_csv(fpath):
    output = defaultdict(list)
    with open(fpath, 'r', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            id = row[0]
            elems = row[1:]
            output[id].append('\n\n'.join(elems).strip())
    return output


for k, v in read_csv("test.csv").items():
    print(k, '-' + '\n-'.join(v))
