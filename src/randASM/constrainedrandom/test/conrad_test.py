from constrainedrandom import RandObj

regs = ["t0","t1","t2","t3"]
class inst(RandObj):
    def __init__(self):
        super().__init__()
        self.add_rand_var('register',domain=regs)
        self.reg_dir = {"r":self.register}

add = inst()
add.randomize()

class a():
    type = "a"
    def __init__(self):
        pass

class b():
    type = "b"
    def __init__(self):
        pass

class c():
    type = "c"
    def __init__(self):
        pass

regs_cls = [a,b,c]

class rand_cls(RandObj):
    def __init__(self):
        super().__init__()
        self.add_rand_var('rnd_cls',domain=regs_cls)
        def is_of_type(x):
            return x.type == "a"
        self.add_constraint(is_of_type,('rnd_cls',))

    def post_randomize(self):
        self.rnd_cls = self.rnd_cls()

my_cls = rand_cls()
my_cls.randomize()
print(my_cls.rnd_cls)

