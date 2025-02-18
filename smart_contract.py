class SmartContract:
    def __init__(self):
        # Балансы пользователей
        self.balances = {}

    def create_account(self, address, initial_balance=0):
        """Создание аккаунта с начальным балансом."""
        if address in self.balances:
            print(f"Аккаунт {address} уже существует.")
        else:
            self.balances[address] = initial_balance
            print(f"Аккаунт {address} создан с балансом {initial_balance} токенов.")

    def transfer(self, sender, receiver, amount):
        """Перевод токенов между аккаунтами."""
        if sender not in self.balances:
            print(f"Аккаунт {sender} не существует.")
            return
        if receiver not in self.balances:
            print(f"Аккаунт {receiver} не существует.")
            return
        if self.balances[sender] < amount:
            print(f"Недостаточно средств на аккаунте {sender}.")
            return

        # Выполняем перевод
        self.balances[sender] -= amount
        self.balances[receiver] += amount
        print(f"Перевод {amount} токенов от {sender} к {receiver} выполнен.")

    def get_balance(self, address):
        """Получение баланса аккаунта."""
        if address in self.balances:
            return self.balances[address]
        else:
            print(f"Аккаунт {address} не существует.")
            return None


if __name__ == "__main__":

    contract = SmartContract()

    contract.create_account("Alice", 1000)
    contract.create_account("John", 500)

    contract.transfer("Alice", "John", 200)

    print(f"Баланс Alice: {contract.get_balance('Alice')}")
    print(f"Баланс John: {contract.get_balance('John')}")
