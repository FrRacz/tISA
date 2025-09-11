from constrainedrandom import RandObj

regs = ["t0","t1","t2","t3"]

class inst(RandObj):
    def __init__(self):
        super().__init__()
        self.add_rand_var('register',domain=regs)
        self.reg_dir = {"r":self.register}

add = inst()
add.randomize()
