from constrainedrandom import RandObj
from randASM.seq_constraints.classes.cl_registers import cl_register
import inspect

class cl_instruction(RandObj):
    def __init__(self,mnemonic:str,temp_constraints:list=[],**operands):
        super().__init__()
        self._mnemonic = mnemonic
        self._temp_constraints = temp_constraints
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
        # Add return call to pass randomized object back
        return self

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
