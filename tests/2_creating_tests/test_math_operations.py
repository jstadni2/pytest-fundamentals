from demos.math_operations import add_numbers


def test_add_numbers():
    assert add_numbers(5, 10) == 15
    assert add_numbers(-1, 1) == 0
    assert add_numbers(-1, -1) == -2, "Adding two negative integers failed."


class TestAddNumbers:
    """
    Test classes may be more intuitive for
    those more familiar with unittest/JUnit.
    """
    def test_positive_integers(self):
        assert add_numbers(5, 10) == 15
    
    def test_negative_positive_integers(self):
        assert add_numbers(-1, 1) == 0
        
    def test_negative_integers(self):
        assert add_numbers(-1, -1) == -2


class TestClassDemoInstance:
    x = 5
    y = 10
    def test_one(self):
        self.x = 10
        assert add_numbers( self.x,  self.y) == 20
    
    # Each test has a unique instance of the class
    def test_two(self):
        assert add_numbers( self.x,  self.y) == 15
        assert self.x == 5
