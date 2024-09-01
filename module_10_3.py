from random import randint
from threading import Thread, Lock

import time

random_number1 = randint(50, 500)
random_number2 = randint(50, 500)


class Bank:
    
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):

        for i in range(100):
            self.balance += random_number1
            print(f'Пополнение: {random_number1}. Баланс: {self.balance}')

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            time.sleep(0.001)

    def take(self):

        n = 0
        while n != 100:
            print(f'Запрос на {random_number2}')

            if random_number2 <= self.balance:
                self.balance -= random_number2
                n += 1
                print(f'Снятие: {random_number2}. Баланс: {self.balance}')

            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
