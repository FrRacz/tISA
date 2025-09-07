from z3 import *

x = Int('x')
y = Int('y')
for _ in range(10):
    print(solve(x < 10, y < 10, x >= 0, y >= 0, x < y).sexpr())
