import vsc

@vsc.randobj
class register():
    self.reg_num = vsc.rand_int_t()
    def __init__(self,reglist:regsiter):
        self._reglist = reglist

    @vsc.constraint
    def reg_in_reglist(self):


class registers():
    self.reglist = list(range(10))
    def __init__(self):
        pass

