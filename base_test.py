# Tests with unittests

# Unit tests supports simple discovery. 
# To be found,  test files must be importable from the top-level

print("Hello Testing!")
def test_pass(): # Had to create subclasses for functions
    assert True # Had to use selfassert

def test_fail():
    assert False