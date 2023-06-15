import unittest
from io import StringIO
from unittest.mock import patch

from main import (
    Espresso, Latte, Cappuccino, Mocha,
    ArabicaBeans, RobustaBeans, ColombianBeans,
    EspressoMachineFactory, LatteMachineFactory, CappuccinoMachineFactory, MochaMachineFactory,
    CoffeeMachine
)

class TestCoffee(unittest.TestCase):
    def test_brew(self):
        espresso = Espresso()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            espresso.brew()
            self.assertEqual(fake_output.getvalue().strip(), "Parzenie espresso...")

    def test_grind(self):
        arabica_beans = ArabicaBeans()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            arabica_beans.grind()
            self.assertEqual(fake_output.getvalue().strip(), "Mielę ziarna arabiki...")

class TestCoffeeMachine(unittest.TestCase):
    def setUp(self):
        self.coffee_machine = CoffeeMachine()

    def test_choose_factory_espresso(self):
        self.coffee_machine.choose_factory('1')
        self.assertIsInstance(self.coffee_machine.factory, EspressoMachineFactory)

    def test_choose_factory_latte(self):
        self.coffee_machine.choose_factory('2')
        self.assertIsInstance(self.coffee_machine.factory, LatteMachineFactory)

    def test_choose_factory_cappuccino(self):
        self.coffee_machine.choose_factory('3')
        self.assertIsInstance(self.coffee_machine.factory, CappuccinoMachineFactory)

    def test_choose_factory_mocha(self):
        self.coffee_machine.choose_factory('4')
        self.assertIsInstance(self.coffee_machine.factory, MochaMachineFactory)

    def test_choose_factory_invalid_choice(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.coffee_machine.choose_factory('5')
            self.assertEqual(fake_output.getvalue().strip(), "Nieprawidłowy wybór kawy!")

    def test_make_coffee_espresso(self):
        self.coffee_machine.choose_factory('1')
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.coffee_machine.make_coffee()
            expected_output = "Mielę ziarna arabiki...\nParzenie espresso...\nSmacznej kawusi :)"
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    def test_make_coffee_no_factory_selected(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.coffee_machine.make_coffee()
            self.assertEqual(fake_output.getvalue().strip(), "Nie wybrano fabryki. Proszę najpierw wybrać rodzaj kawy.")

    def test_make_coffee_invalid_factory(self):
        self.coffee_machine.choose_factory('5')
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.coffee_machine.make_coffee()
            self.assertEqual(fake_output.getvalue().strip(), "Nie wybrano fabryki. Proszę najpierw wybrać rodzaj kawy.")

if __name__ == '__test__':
    unittest.main()