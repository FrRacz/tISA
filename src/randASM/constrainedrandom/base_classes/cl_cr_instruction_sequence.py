from constrainedrandom import RandObj

class meta_instruction(RandObj):
    def __init__(self):
        pass

class cl_instruction_sequence(RandObj):
    def __init__(self,instr_bank):
        super().__init__()
        self.instr_bank = instr_bank
        self.instruction_list = None
        self.add_rand_var('mnemonic_list',domain=self.instr_bank._instr_dict.keys(),length=100)

    def get_instructions(self):
        self.instruction_list = self.instr_bank.get_instruction_list(self.mnemonic_list)

    def randomize_instructions(self):
        for instr in self.instruction_list:
            instr.randomize()

    def get_asm_str(self):
        asm = ""
        for instr in self.instruction_list:
            asm += instr.get_asm_str()
        return asm





