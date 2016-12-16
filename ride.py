'''
ID: romario5
LANG: PYTHON
PROG: ride
'''

def cnt(s):
    r = 1
    for c in s:
        r *= (ord(c) - ord('A') + 1)
    return r % 47

def solve(comet, group):
    if cnt(comet) == cnt(group):
        return "GO"
    return "STAY"

def go():
    problem = 'ride'
    ifile = open(problem + '.in', 'r')
    ofile = open(problem + '.out', 'w')
    try:
        comet = ifile.readline()
        group = ifile.readline()
        r = solve(comet, group)
        ofile.writelines(r)
    finally:
        ofile.close()

# print solve('COMETQ', 'HVNGAT')
go()
