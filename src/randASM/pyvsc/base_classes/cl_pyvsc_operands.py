import vsc

class cl_label_op():
    def __init__(self):
        pass

class cl_memory_location_op():
    def __init__(self):
        pass

@vsc.randobj
class cl_immediate():
    def __init__(self,size):
        self._val = vsc.rand_int_t(w=size)

    @vsc.constraint
    def unsigned(self):
        self._val >= 0

    def get_asm_str(self):
        return f"{hex(self._val)}"

if __name__ == "__main__":
    imm = cl_immediate(10)
    imm.randomize()
    print(f"Imm: {imm.get_asm_str()}")
