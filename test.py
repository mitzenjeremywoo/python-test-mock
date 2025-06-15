import unittest 
from echo import Echo, Dog, Cat, Animal
from unittest.mock import Mock

class EchoTestDog(unittest.TestCase):
    
    def test_target_hello(self):
        animal = Dog()
        target = Echo(animal)
        result = target.sayHello()
        self.assertEqual(result, "woof")
    
class EchoTestCat(unittest.TestCase):
    
    def test_target_hello(self):
        animal = Cat()
        target = Echo(animal)
        result = target.sayHello()
        self.assertEqual(result, "meow")

## Testing Echo Service 
class EchoTestService(unittest.TestCase):
    
    def test_target_hello(self):
        mockAnimal = Mock()

        ## fake the sayHello method to return a hard coded value "Grrr"
        mockAnimal.sayHello.return_value = "Grrr"
        
        target = Echo(mockAnimal)
        result = target.sayHello()
        
        self.assertEqual(result, "Grrr")
        mockAnimal.sayHello.assert_called_once()

    # test to fake an exception; Exception type here could be too general. It should be something like ValueError
    # or SystemError
    def test_target_hello_error(self):

        mockAnimal = Mock()
        mockAnimal.sayHello.side_effect = Exception("")

        with self.assertRaises(Exception):
            target = Echo(mockAnimal)
            result = target.sayHello()
        

if __name__ == '__main__':
    unittest.main()
