# Tests with unittests

# Unit tests supports simple discovery. 
# To be found,  test files must be importable from the top-level

print("Hello Testing!")
def test_pass(): # Had to create subclasses for functions
    assert True # Had to use selfassert

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }