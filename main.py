from rational import Rational
from rational_list import RationalList

def read_file(filename):
    rlist = RationalList()
    with open(filename, 'r') as f:
        for line in f:
            for item in line.split():
                if '/' in item:
                    n, d = item.split('/')
                    rlist.add(Rational(int(n), int(d)))
                else:
                    rlist.add(Rational(int(item)))
    return rlist

def save_file(rlist, filename):
    with open(filename, 'w') as f:
        for r in rlist:
            f.write(str(r) + ' ')

inputs = ["input01 (6).txt", "input02 (5).txt", "input03 (5).txt"]
outputs = ["output01.txt", "output02.txt", "output03.txt"]

for inp, out in zip(inputs, outputs):
    lst = read_file(inp)
    save_file(lst, out)
