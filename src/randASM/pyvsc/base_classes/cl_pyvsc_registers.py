import vsc
from collections import Counter

class register_bank():
    def __init__(self,size:int,prefix:str):
        self._size = size
        self._reglist = vsc.list_t(vsc.int_t(),self._size)
        self._prefix = prefix
        for i in range(size):
            self._reglist[i] = i

    def get_asm_str(self,reg_nr:int):
        return f"{self._prefix}{reg_nr}"

@vsc.randobj
class cl_register():
    def __init__(self,reg_bank:register_bank):
        self._reg_bank = reg_bank
        self._reg_num = vsc.rand_int_t()

    @vsc.constraint
    def reg_in_reglist(self):
        self._reg_num.inside(vsc.rangelist(self._reg_bank._reglist))

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

