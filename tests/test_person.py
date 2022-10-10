
import unittest

from src.person import Person

class PersonTest(unittest.TestCase):

    p1: Person = Person("mario")
    p2: Person = Person("luigi", 20, 1000)
    p3: Person = Person("peach", 30, 500)
    p4: Person = Person("bowser", 15, 100)

    def test_init_person_defaults(self):
        self.assertEqual(self.p1.name, "mario")
        self.assertEqual(self.p1.age, 0)
        self.assertEqual(self.p1.money, 0)

    def test_init_person_custom_age_money(self):
        self.assertEqual(self.p2.name, "luigi")
        self.assertEqual(self.p2.age, 20)
        self.assertEqual(self.p2.money, 1000)

    def test_celebrates_birthday(self):
        self.p3.celebrates_birthday()

        self.assertEqual(self.p3.age, 31)

    def test_earn_money(self):
        self.p4.earns_money(500)

        self.assertEqual(self.p4.money, 600)

    def test_spend_money(self):
        self.p3.spends_money(200)

        self.assertEqual(self.p3.money, 300)

