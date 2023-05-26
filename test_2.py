import mock_testing #Our test target
from mock_testing import returnVal

def testCal():
    assert mock_testing.Calculator.sum(1, 2) == 3

def testObjectMock(mocker):
    mocker.patch.object(mock_testing, 'CONSTANT_VAL', 400)
    assert returnVal() == 200

# We can patch our slow API calls
def testFunctiontMock(mocker):
    mocker.patch.object('mock_testing.api_call', return_value="Mocked API!")
    call = mock_testing.slowAPI()
    assert call == 200



# returnVal has a wait, we do not want to slow down our tests
# Break out the API (integration) and value tests
# MagicMock - a placeholder
    # Mock a constant, object, function
    # You want to mokc where the object is import INTO not FROM
    # So if you already import B into A, you patch in A