import mock_testing #Our test target

def testCal():
    assert mock_testing.Calculator.sum(1, 2) == 3

def testVal(mocker):
    # returnVal has a wait, we do not want to slow down our tests
    # Break out the API (integration) and value tests
    # MagicMock - a placeholder
        # Mock a constant, object, function
        # You want to mokc where the object is import INTO not FROM
        # So if you already import B into A, you patch in A
    mocker.patch.object(mock_testing.returnVal, 'CONSTANT_VAL', 400)
    assert mock_testing.returnVal() == 200