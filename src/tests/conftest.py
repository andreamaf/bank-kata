
from unittest.mock import patch
from datetime import date
from .. import bank

import pytest


@pytest.fixture
def account():
    return bank.Account()


@pytest.fixture
def account_start_balance():
    return bank.Account(start_balance=789)


@pytest.fixture
def acceptance_account():
    account = bank.Account()

    with patch('src.bank.date') as mock_date:
        mock_date.today.return_value = date(2012, 1, 10)
        account.deposit(1000)

    with patch('src.bank.date') as mock_date:
        mock_date.today.return_value = date(2012, 1, 13)
        account.deposit(2000)

    with patch('src.bank.date') as mock_date:
        mock_date.today.return_value = date(2012, 1, 14)
        account.withdrawal(500)

    return account

