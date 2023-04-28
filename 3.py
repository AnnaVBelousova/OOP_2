# С этой задачей я еще не разобралась 

class TypedMeta(type):
    a = None

    def __call__(cls, clsname, bases, clsdict):
        if TypedMeta.a is None:
            TypedMeta.a = super().__new__(clsname, bases, clsdict)
        return TypedMeta.a

class MyClass(metaclass=TypedMeta):
    pass
    def method_1(self):
        pass
    def method_2(self):
        pass
obj_1 = MyClass()
obj_2 = MyClass()

print(obj_1 is obj_2)  # True