def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150


def test_deposit_twice_increases_balance(account):
    account.deposit(50)
    account.deposit(25)
    assert account.balance == 175