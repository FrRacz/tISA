from constrainedrandom import RandObj
from collections import Counter

class register_bank():
    def __init__(self,size:int,prefix:str):
        self._size = size
        self._reglist = list(range(self._size))
        self._prefix = prefix

    def get_asm_str(self,reg_nr:int):
        return f"{self._prefix}{reg_nr}"

class cl_register(RandObj):
    def __init__(self,reg_bank:register_bank):
        super().__init__()
        self._reg_bank = reg_bank
        self.add_rand_var("_reg_num", domain=range(self._reg_bank._size))
        self.add_constraint(self.reg_in_reglist,('_reg_num',))

    def reg_in_reglist(self, reg_num):
        return reg_num in self._reg_bank._reglist

    def get_asm_str(self):
        return self._reg_bank.get_asm_str(self._reg_num)

if __name__ == "__main__":
    reg_bank = register_bank(prefix='t',size=10)
    test_reg = cl_register(reg_bank=reg_bank)
    print(f"reg_bank: {reg_bank._reglist}")

    choice = []
    n = 1000
    for _ in range(n):
        test_reg.randomize()
        choice.append(int(test_reg._reg_num))

    counts = Counter(choice)
    for number,fq in sorted(counts.items()):
        print(f"{number}: {fq/n*100}%")

    # additional constr on reg
    def less_than_five(x):
        return x < 5
    test_reg.add_constraint(less_than_five,('_reg_num',))
    choice = []
    n = 1000
    for _ in range(n):
        test_reg.randomize()
        choice.append(int(test_reg._reg_num))

    counts = Counter(choice)
    for number,fq in sorted(counts.items()):
        print(f"{number}: {fq/n*100}%")
