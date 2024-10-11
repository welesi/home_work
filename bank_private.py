class BankAccount: # Класс BankAccount определяет банковский счет с определенным начальным балансом
    def __init__(self, balance):  # Это метод-конструктор, который вызывается при создании нового объекта класса BankAccount
        self._balance = balance # приватная переменная
    def deposit(self, amount): # Этот метод позволяет пользователю вносить деньги на счет
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount): # Этот метод позволяет пользователю снимать деньги со счета
        if amount <= self._____balance:
            self._balance -= amount
        else:
            print("Недостаточно средств")
    def get_balance(self): # Этот метод возвращает текущее значение приватной переменной _balance
        return self.___balance

account=BankAccount (1000) # Создается объект account класса BankAccount с начальным балансом 1000
account.deposit(500) # Вызывается метод deposit(500), который увеличивает баланс на 500
print(account.get_balance()) # Вызывается метод get_balance(), который возвращает текущий баланс
# Попытка непосредственного обращения к приватной переменной _balance вызовет ошибку, так как эта переменная является приватной.
