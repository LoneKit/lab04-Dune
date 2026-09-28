import pytest
from bank import BankAccount

@pytest.fixture
def account():
    return BankAccount(100)

def test_deposit_increases_balance(account):
    assert account.deposit(50) == 150

def test_deposit_twice_increases_balance(account):
    account.deposit(50)
    assert account.deposit(25) == 175