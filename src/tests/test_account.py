
import pytest
from ..bank import Account


@pytest.fixture
def account():
    return Account()


def test_acceptance_test(account):

    depo1 = (1000, '10/01/2012')
    account.deposit(*depo1)

    depo2 = (2000, '13/01/2012')
    account.deposit(*depo2)

    withdr1 = (500, '14/01/2012' )
    account.withdrawal(*withdr1)

    expected = [
                "14/01/2012\t|| -500\t|| 2500",
                "13/01/2012\t|| 2000\t|| 3000",
                "10/01/2012\t|| 1000\t|| 1000"
               ]

    assert account.get_transactions_history() == expected
