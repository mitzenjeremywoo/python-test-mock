class Animal:
    def __init__(self):
        pass

    def sayHello() -> str: 
        pass
      
class Dog(Animal):
    def __init__(self):
        pass

    def sayHello(self) -> str:
        return "woof"

class Cat(Animal):
    def __init__(self):
        pass

    def sayHello(self) -> str:
        return "meow"

class Echo:
    target: Animal

    def __init__(self, target: Animal):
        self.target = target

    def sayHello(self) -> str:
        return self.target.sayHello()