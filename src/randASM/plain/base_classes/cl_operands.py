class cl_operand():
    def __init__(self):
        pass
    def get_asm_str(self):
        pass

class cl_label_op(cl_operand):
    def __init__(self):
        pass

class cl_memory_location_op(cl_operand):
    def __init__(self):
        pass

class cl_immediate_op(cl_operand):
    def __init__(self):
        pass

class cl_register_op(cl_operand):
    def __init__(self,name):
        self._name = name

