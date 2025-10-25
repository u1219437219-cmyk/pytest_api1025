import pytest
from utils.api_request import send_post

@pytest.mark.parametrize("case", [
    {"username": "admin", "password": "123456", "expected_code": 200},
    {"username": "admin", "password": "000000", "expected_code": 401},
    {"username": "wronguser", "password": "123456", "expected_code": 401}
])
def test_login(base_url, case):
    url = f"{base_url}/login"
    res = send_post(url, {"username": case["username"], "password": case["password"]})
    assert res["code"] == case["expected_code"]
