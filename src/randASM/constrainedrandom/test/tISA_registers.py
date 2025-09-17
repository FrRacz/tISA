from randASM.constrainedrandom.base_classes.cl_registers import *

class t0(cl_register):
    def __init__(self):
        super().__init__("t0")

class t1(cl_register):
    def __init__(self):
        super().__init__("t1")

class t2(cl_register):
    def __init__(self):
        super().__init__("t2")

class t3(cl_register):
    def __init__(self):
        super().__init__("t3")

class t4(cl_register):
    def __init__(self):
        super().__init__("t4")

class t5(cl_register):
    def __init__(self):
        super().__init__("t5")

class t6(cl_register):
    def __init__(self):
        super().__init__("t6")

class t7(cl_register):
    def __init__(self):
        super().__init__("t7")

class t8(cl_register):
    def __init__(self):
        super().__init__("t8")

class t9(cl_register):
    def __init__(self):
        super().__init__("t9")

class t10(cl_register):
    def __init__(self):
        super().__init__("t10")

class t11(cl_register):
    def __init__(self):
        super().__init__("t11")

class t12(cl_register):
    def __init__(self):
        super().__init__("t12")

class t13(cl_register):
    def __init__(self):
        super().__init__("t13")

class t14(cl_register):
    def __init__(self):
        super().__init__("t14")

class t15(cl_register):
    def __init__(self):
        super().__init__("t15")

tISA_register_bank = cl_register_bank('base_regs')
tISA_register_bank.register_register(
        t0=t0,
        t1=t1,
        t2=t2,
        t3=t3,
        t4=t4,
        t5=t5,
        t6=t6,
        t7=t7,
        t8=t8,
        t9=t9,
        t10=t10,
        t11=t11,
        t12=t12,
        t13=t13,
        t14=t14,
        t15=t15
        )
