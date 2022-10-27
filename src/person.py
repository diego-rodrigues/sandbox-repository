
class Person:
    def __init__(self, name, age = 0, money = 0):
        self.name = name
        self.age = age
        self.money = money

    def celebrates_birthday(self):
        self.age+= 3

    def earns_money(self, money_earned):
        if money_earned > 0:
            self.money += money_earned
        else:
            raise Exception("Didn't earn anything.")

    def spends_money(self, money_spent):
        if money_spent > 0 and self.money >= money_spent:
            self.money -= money_spent
        else:
            raise Exception("Can't spend this amount of money.")
