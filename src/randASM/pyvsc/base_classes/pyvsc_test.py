import vsc

@vsc.randobj
class ident():
    def __init__(self,name):
        self.i = name




@vsc.randobj
class test_class():
    def __init__(self,ident_list):
        self.ident = vsc.rand_attr(ident("ident_test_class"))
        self.ident_list = ident_list

    @vsc.constraint
    def in_ident_list(self):
        self.ident in self.ident_list

if __name__ == "__main__":
    hello = ident("hello")
    world = ident("world")
    this = ident("this")
    test = ident("test")

    ident_list = vsc.list_t(vsc.rand_attr(ident("ident_list")))
    ident_list.append(hello)
    ident_list.append(world)
    ident_list.append(this)
    ident_list.append(test)

    for _ in range(10):
        instance = test_class(ident_list)
        instance.ranzomide()
        print(instance.ident.i)
