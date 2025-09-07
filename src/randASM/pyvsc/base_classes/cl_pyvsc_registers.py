import vsc

class register_bank():
    def __init__(self,size:int,prefix:str):
        self._reglist = vsc.list_t(vsc.int_t(),size)
        self._prefix = prefix
        for i in range(size):
            self._reglist[i] = i
        pass

    def get_asm_str(self,reg_nr:int):
        return f"{self._prefix}{reg_nr}"

@vsc.randobj
class cl_register():
    def __init__(self,reg_bank:register_bank):
        self._reg_bank = reg_bank
        self._reg_num = vsc.rand_int_t()

    @vsc.constraint
    def reg_in_reglist(self):
        self._reg_num in self._reg_bank._reglist

    def get_asm_str(self):
        return self._reg_bank.get_asm_str(self._reg_num)

if __name__ == "__main__":
    reg_list = register_bank(size=10)
    test_reg = cl_register(prefix='t',reglist=reg_list)
    for _ in range(10):
        test_reg.randomize()
        print(test_reg.get_asm_string())
