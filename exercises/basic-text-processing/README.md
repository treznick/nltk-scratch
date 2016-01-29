## The anatomy of a test:
```python
#First we import unittest and whatever we want to test
import unittest
from <your python file> import <your thing you want to test>

#then we define a class that inherits from unittest.TestCase
class TestSomething(unittest.TestCase):
#then we define methods in that class that test our code
    def test_a_thing_works(self):
        #here is our input
        input = "Foobar"
        #here is the thing we want to test
        test_object = SomethingWeImported(input)
        #here is our expected result
        expectation = "Expected Output"
        #and here is our test
        self.assertEqual(expectation, test_object.method_we_want_to_test())

```                                     

Ok, so how about a real example:

Let's say we have a file called `calculator.py` that has the following code:
```python
class Calculator
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def add(self):
        return (self.first_number + self.second_number)

```
This is a very simple python object. We can construct it using it's `__init__` method with two numbers, and then call `add()` to return the sum of those two numbers

We could write a test for that class in `test_calculator.py`
```python
class TestCalculator(unittest.TestCase):
    def test_add(self):
        calculator = Calculator(3,5)
        expectation = 8
        self.assertEqual(expectation, calculator.add())

```

This way, if we wanted to add a `multiply()` method to the `Calculator` class, we can do so by first writing a failing test
```python
# in TestCalculator
    def test_multipy(self):
        calculator = Calculator(3,5)
        expectation = 15
        self.assertEqual(expectation, calculator.add())

```

Watch it fail, and then write the method and make it pass
```python
#in Calculator
    def multiply(self):
        return (self.first_number * self.second_number)

```

## How to run these tests:

  1) run: `python -m unittest test_basic_processing`
  2) The test script will run and produce an output of passing and failing tests.
  3) Each test gives the `tokenize` method in `Tokenizer` (defined in `tokenizer.py`) a different input
    * It's your job to make all of these tests pass.
    * You need to do that by implementing the `tokenize` method inside of the `Tokenizer` class in `tokenizer.py`
      * Right now, the method just prints "Implement Me!", change that so that it passes all of the tests
    * The failures will return an AssertionError, which is what the testing framework raises when the assertion defined in the tests don't pass.
