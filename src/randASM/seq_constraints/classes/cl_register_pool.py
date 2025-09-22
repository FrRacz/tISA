class cl_register_pool():
    def __init__(self,name):
        self._name = name
        self._reg_dict = {}

    def register_register(self, **registers):
        for reg_name, reg_cls in registers.items():
            self._reg_dict[reg_name] = reg_cls

    def get_domain(self):
        return self._reg_dict.values()
