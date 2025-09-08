from constrainedrandom import RandObj

class cl_label_op():
    def __init__(self):
        pass

class cl_memory_location_op():
    def __init__(self):
        pass

class cl_immediate(RandObj):
    def __init__(self,size):
        super().__init__()
        self._size = size
        self.add_rand_var('_val',domain=range(2**self._size))

    def get_asm_str(self):
        return f"{hex(self._val)}"

if __name__ == "__main__":
    imm = cl_immediate(10)
    imm.randomize()
    print(f"Imm: {imm.get_asm_str()}")
