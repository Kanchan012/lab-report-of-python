from abc import ABC,abstractmethod
class Parent(ABC):
    @abstractmethod
    def display(self):
        pass
    def show(self):
        pass
class Child(Parent):
    def display(self):
        print("This is display method")
    def show(self):
        print("This is show method")   
obj=Child()  
obj.display()   
obj.show()         