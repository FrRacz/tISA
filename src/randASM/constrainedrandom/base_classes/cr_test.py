from constrainedrandom import RandObj

INSTRUCTIONS = ["add", "sub", "jal", "lw", "sw"]
ALLOWED_INSTRUCTIONS = ["add", "sub", "jal", "lw", "sw"]

class InstrGen(RandObj):
    def __init__(self):
        super().__init__()
        # domain can be any iterable of allowed values
        self.add_rand_var('instr', domain=INSTRUCTIONS)
        self.add_constraint(self.is_allowed,('instr',))
    def is_allowed(self,instr):
        return instr in ALLOWED_INSTRUCTIONS

if __name__ == "__main__":
    g = InstrGen()

    for _ in range(8):
        g.randomize()
        print(g.instr)
    ALLOWED_INSTRUCTIONS = ["lw","sw"]
    print("-"*8)
    for _ in range(8):
        g.randomize()
        print(g.instr)
