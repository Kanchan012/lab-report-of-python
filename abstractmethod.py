from abc import ABC,abstractmethod
class Parent(ABC):
    @abstractmethod
    def display(self):
        pass
    def show(self):
        print("This is concrete method")
class Child(Parent):
    def display(self):
        print("This is abstract method") 
obj=Child()  
obj.display()
obj.show()            