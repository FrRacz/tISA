from constrainedrandom import RandObj

class cl_instruction_bank():
    """
    Class to hold all instructions of a ISA.
    """
    def __init__(self):
        self._instr_dict = {}

    def register_instruction(self, **instructions):
        """
        Add a new instruction to the instruction dictionary
        """
        for mnemonic, instr_cls in instructions.items():
            self._instr_dict[mnemonic] = instr_cls

class cl_instruction_sequence():
    def __init__(self):
        self._instr_stream = []
        self._asm_stream = []

    def randomize(self):
        for instr in self._instr_stream:
            if isinstance(instr,cl_meta_instruction):
                instr.resolve_required()

        for instr in self._instr_stream:
            if isinstance(instr,cl_instruction):
                instr.randomize()
                self._asm_stream.append(instr)
            elif isinstance(instr,cl_meta_instruction):
                instr_ret = instr.randomize()
                self._asm_stream.append(instr_ret)




class cl_meta_instruction(RandObj):
    def __init__(self,instr_pool,parent_sequence:cl_instruction_sequence):
        super().__init__()
        self.add_rand_var('instr',domain=instr_pool)
        self.parent_sequence = parent_sequence
        self._required = []

    def add_required_instr(self,instr,location:range):
        self._required.attach((instr,location))

    def resolve_required(self):
        for instr, location in self._required:
            idx = self.parent_sequence.instr_stream.index(self)
            offset = random.choice(location)
            self.parent_sequence.instr_stream.insert(idx+offset,instr)

    def randomize(self):
        super().randomize()
        return self.instr().randomize()

class cl_instruction(RandObj):
    def __init__(self,mnemonic:str,temp_constraints:list,**operands):
        super().__init__()
        self._mnemonic = mnemonic
        self._temp_constraint = temp_constraints
        self._op_banks = {}
        self._op_names = []
        for op_name, op_bank in operands.items():
            self._op_names.append(op_name)
            self._op_banks[op_name] = op_bank
            self.add_rand_var(op_name,domain=op_bank.get_domain())

    def add_temp_constraints(self,*constraints):
        """
        Adds a numer of temporary constraints to the instruction.
        """
        for const in constraints:
            #TODO: check if instruction has the operand type
            self._temp_constraints.append(const)

    def get_mnemonic(self):
        return self._mnemonic


    def remove_temp_constraints(self,*operands):
        """
        Removes the temporary constraints for the specified operands.
        !Also removes multivariable constraints if the operand is present.
        """
        for op in operands:
            self._temp_constraints = [const for const in self._temp_constraints
                                      if not any(op in rand_vars for rand_vars in const[1])]

    def randomize(self):
        super().randomize(with_constraints=self._temp_constraints)

    def post_randomize(self):
        for op in self._op_names:
            op_cls = getattr(self, op)
            # Check if the operand needs to be instantiated
            if inspect.isclass(op_cls):
                setattr(self,op,op_cls())

    def get_asm_str(self):
        asm = f'{self._mnemonic} '
        # only random vars in the instruction should be the
        for op in self._op_names:
            op_cls = getattr(self, op)
            if isinstance(op_cls,cl_register):
                asm += f"{getattr(op_cls,'get_asm_str')()}, "
            elif isinstance(op_cls,int):
                asm += f"{hex(op_cls)}, "
        asm = asm[:-2] + '\n'
        return asm
