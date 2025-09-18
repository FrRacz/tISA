class Item:
    def __init__(self,name:str,parent_list:list):
        self.name = name
        self._list = parent_list

    def find_self(self):
        idx = self._list.index(self)
        return f"{self.name} at position {idx}"

    def __str__(self):
        return self.name

test_list = []
test_list.append(Item(name='a',parent_list=test_list))
test_list.append(Item(name='b',parent_list=test_list))
test_list.append(Item(name='c',parent_list=test_list))
print(test_list[1].find_self())

