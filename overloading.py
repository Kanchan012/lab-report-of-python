class OperatorOverloadingDemo:
    def __init__(self, a):
        self.a = a
    def __add__(self, b):
        return self.a + b.a
class OperatorOverloadingDemoA:
    def __init__(self, a):
        self.a = a
obj=OperatorOverloadingDemo(10)
obj1=OperatorOverloadingDemoA(20)
print(obj+obj1)           