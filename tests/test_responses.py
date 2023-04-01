from rentomatic.responses import ResponseSucess

def test_response_success_is_true():
    assert bool(ResponseSucess()) is True
