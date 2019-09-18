
import pytest
from ..bank import Account


@pytest.fixture
def account():
    return Account()


@pytest.fixture
def account_start_balance():
    return Account(start_balance=789)


@pytest.fixture
def acceptance_account():
    account = Account()

    depo1 = (1000, '10/01/2012')
    account.deposit(*depo1)

    depo2 = (2000, '13/01/2012')
    account.deposit(*depo2)

    withdr1 = (500, '14/01/2012' )
    account.withdrawal(*withdr1)
    return account


def test_deposit_transaction(account):
    account.deposit(1000, '01/01/2001')
    assert account.balance == 1000


def test_deposit_transaction_start_balance(account_start_balance):
    account_start_balance.deposit(1000, '01/01/2001')
    assert account_start_balance.balance == 1789



def test_transactions_history(acceptance_account):
    expected = [
                "14/01/2012\t|| -500\t|| 2500",
                "13/01/2012\t|| 2000\t|| 3000",
                "10/01/2012\t|| 1000\t|| 1000"
               ]
    assert acceptance_account.get_transactions_history() == expected


def test_acceptance_test(acceptance_account, capsys):
    acceptance_account.print_statement()
    expected = ("14/01/2012\t|| -500\t|| 2500\n"
                "13/01/2012\t|| 2000\t|| 3000\n"
                "10/01/2012\t|| 1000\t|| 1000\n")
    captured = capsys.readouterr()
    assert captured.out == expected
