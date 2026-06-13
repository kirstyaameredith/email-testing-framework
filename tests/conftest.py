import pytest
from src.mailpit_client import MailpitClient

@pytest.fixture
def mailpit():
    client = MailpitClient()
    client.clear_inbox()   # Clean inbox before each test
    return client
