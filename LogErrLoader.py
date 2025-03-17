import csv
import numpy as np

def LoadDNDSLogErr(fname):
    with open(fname, "r") as f:
        reader = csv.reader(f)
        fields = next(reader)
        # print(fields)
        out = {}
        for field in fields:
            if len(field):
                out[field] = []
        for row in reader:
            for [idx, v] in enumerate(row):
                field = fields[idx]
                if len(field):
                    try:
                        v = float(v)
                    except ValueError:
                        v = float('nan')
                    out[field].append(v)
    for col in out:
        col = np.array(col)
    return out
