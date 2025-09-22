from constrainedrandom import RandObj
from randASM.seq_constraints.classes.cl_register_pool import cl_register_pool
from collections import Counter

class cl_register():
    def __init__(self,reg_name):
        self._reg_name = reg_name
    def get_asm_str(self):
        return self._reg_name

if __name__ == "__main__":

    class t0(cl_register):
        type = 't0'
        def __init__(self):
            super().__init__('t0')

    class t1(cl_register):
        type = 't1'
        def __init__(self):
            super().__init__('t1')

    class t2(cl_register):
        type = 't0'
        def __init__(self):
            super().__init__('t2')

    reg_bank = cl_register_pool('gp_reg')
    reg_bank.register_register(
            t0=t0,
            t1=t1,
            t2=t2,
            )

    class instr(RandObj):
        def __init__(self,domain):
            super().__init__()
            self.add_rand_var('r0',domain=domain)
            self.add_rand_var('r1',domain=domain)
            def a_is_not_b(a,b):
                return a != b
            def same_type(a,b):
                return a.type == b.type
            self.add_constraint(a_is_not_b,('r0','r1'))
            self.add_constraint(same_type,('r0','r1'))

    test_i = instr(domain=reg_bank._reg_dict.values())
    print(test_i._random_vars)
    test_i.randomize()
    print(f'r0: {test_i.r0}, r1: {test_i.r1}')

