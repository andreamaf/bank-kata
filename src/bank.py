
class Account():
    def __init__(self, start_balance=0):
        self._balance = start_balance
        self._transactions_history = []

    @property
    def balance(self):
        return self._balance

    def get_transactions_history(self):
        str_history = ["%s\t|| %s\t|| %s" % (date, amount, balance)
                        for date, amount, balance in self._transactions_history]
        return str_history[::-1]

    def deposit(self, amount):
        self._balance += amount
        self._transactions_history.append((date, amount, self._balance))

    def withdrawal(self, amount):
        self._balance -= amount
        self._transactions_history.append((date, -amount, self._balance))

    def print_statement(self):
        for transaction in self.get_transactions_history():
            print (transaction)
