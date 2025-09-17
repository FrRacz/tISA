from randASM.constrainedrandom.base_classes.cl_registers import cl_register
import inspect
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


    def get_instruction(self,mnemonic):
        """
        Not in use
        """
        instr = self._instr_dict[mnemonic]()
        return instr

    def get_instruction_list(self,instruction_list:list):
        """
        Not in use
        """
        instructions = []
        for instr_mn in instruction_list:
            instructions.append(self.get_instruction(instr_mn))
        return instructions



class cl_instruction(RandObj):
    """
    Instruction baseclass, used derive instruction classes.

    Derived from constraindrandoms RandObj

    Attibutes:
        _mnemonic (str): ASM indentifier of the instruction
        _temp_constraints (list of constraindrandom constraints):
            Temporary constraints, applied at randomization with `with_constraints`.
            New constraints can be added with add_temp_constraints.
            Constraints for a specific operand can be removed with remove_temp_constraints.
    """

    def __init__(self,mnemonic:str,**operands):
        """
        Args:
            mnemonic (str): ASM indentifier of the instruction
            **operands (operand_name: operand_bank): Operands of the instruction
        """
        super().__init__()
        self._mnemonic = mnemonic
        self._temp_constraints = []
        self._op_banks = {}
        self._op_names = []
        self.label = None
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

if __name__ == "__main__":
    # TODO: Make small directed test
    pass
