import pytest
import yaml

@pytest.fixture(scope="session")
def base_url():
    return "http://example.com/api"

@pytest.fixture(scope="session")
def login_data():
    with open("data/login_data.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)
