import random

class cl_instruction_bank():
    def __init__(self,*args):
        self._instr_dict = {}
        # populate the instruction dictornary
        for instr in args:
            self._instr_dict[instr.__name__] = instr #careful this is just a rererence

    def get_rand_intruction(self):
        instr = random.choice(list(self._instr_dict.values()))
        return instr()



class cl_instruction():
    def __init__(self,name):
        self._name = name
        pass

    def get_asm_str(self):
        pass

    def get_name(self):
        return self._name

    def randomize(self):
        pass
