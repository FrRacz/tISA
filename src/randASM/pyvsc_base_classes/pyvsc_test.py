import vsc

class instance():
    def __init__(self,name: str):
        self._name = name

class inst_bank():
    def __init__(self,*args):
        for arg in args:
            self.inst_list.append(arg):
