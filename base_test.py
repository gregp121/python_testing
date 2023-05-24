# Tests with unittests

# Unit tests supports simple discovery. 
# To be found,  test files must be importable from the top-level

class pyTesting():
    print("Hello world!")
    def test_pass(self): # Had to create subclasses for functions
        self.assertTrue(True) # Had to use selfassert

    def test_fail(self):
        self.assertTrue(False)