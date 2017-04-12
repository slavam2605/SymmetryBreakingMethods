import sys
sys.path.append("..")
from test_suite import run_test
import os


if __name__ == '__main__':
    os.chdir("..")
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    m = None
    bfs = False
    max_deg = False
    weights = False
    degs = False
    lex = False
    unavoid = False
    unsat = False
    max_seconds = 3600
    solver = 'treengeling'
    args = iter(sys.argv[3:])
    for arg in args:
        if arg == 'm':
            m = int(next(args))
        elif arg == 'max_seconds':
            max_seconds = int(next(args)) 
        elif arg == 'solver':
            solver = next(args)
        elif arg == 'bfs':
            bfs = True
        elif arg == 'max_deg':
            max_deg = True
        elif arg == 'weights':
            weights = True
        elif arg == 'degs':
            degs = True
        elif arg == 'lex':
            lex = True
        elif arg == 'unavoid':
            unavoid = True
        elif arg == 'unsat':
            unsat = True
        else:
            print "Unknown argument: " + arg
            sys.exit(1)
    for n in xrange(n1, n2 + 1):
        run_test("dumps/dump1", n, m, bfs, max_deg, weights, degs, lex, unavoid, unsat, max_seconds, solver)



