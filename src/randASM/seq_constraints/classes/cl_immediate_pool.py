class cl_immediate_pool():
    def __init__(self,size):
        self._size = size
    def get_domain(self):
        return range(0,self._size**2)
