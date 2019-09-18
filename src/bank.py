
class Account():
    def __init__(self, start_balance=0):
        self.balance = start_balance
        self.transactions_history = []

    def get_transactions_history(self):
        str_history = ["%s\t|| %s\t|| %s" % (date, amount, balance)
                        for date, amount, balance in self.transactions_history]
        return str_history[::-1]

    def deposit(self, amount, date):
        self.balance += amount
        self.transactions_history.append((date, amount, self.balance))

    def withdrawal(self, amount, date):
        self.balance -= amount
        self.transactions_history.append((date, -amount, self.balance))

    def print_statement(self):
        for transaction in self.get_transactions_history():
            print (transaction)
