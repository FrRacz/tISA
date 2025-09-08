import random
from constrainedrandom import RandObj

INSTRUCTIONS = ["add", "sub", "jal", "lw", "sw"]

class InstrGen(RandObj):
    def __init__(self):
        super().__init__()
        # domain can be any iterable of allowed values
        self.add_rand_var('instr', domain=INSTRUCTIONS)

if __name__ == "__main__":
    g = InstrGen()
    for _ in range(8):
        g.randomize()
        print(g.instr)

