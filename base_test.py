# Tests with unittests

# Unit tests supports simple discovery. To be found, all test files must be in modules or packages importable from the top-level

from unittest import TestCase
class pyTesting(testCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)