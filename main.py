from abc import ABC, abstractmethod

# Abstrakcyjne klasy produktów
class Coffee(ABC):
    @abstractmethod
    def brew(self):
        pass

class CoffeeBeans(ABC):
    @abstractmethod
    def grind(self):
        pass

# Abstrakcyjna fabryka
class CoffeeMachineFactory(ABC):
    @abstractmethod
    def create_coffee(self) -> Coffee:
        pass

    @abstractmethod
    def create_coffee_beans(self) -> CoffeeBeans:
        pass

# Konkretne klasy produktów
class Espresso(Coffee):
    def brew(self):
        print("Parzenie espresso...")

class Latte(Coffee):
    def brew(self):
        print("Parzenie kawy latte...")

class Cappuccino(Coffee):
    def brew(self):
        print("Parzenie kawy cappuccino...")

class Mocha(Coffee):
    def brew(self):
        print("Parzenie kawy mocha...")

class ArabicaBeans(CoffeeBeans):
    def grind(self):
        print("Mielę ziarna arabiki...")

class RobustaBeans(CoffeeBeans):
    def grind(self):
        print("Mielę ziarna robusty...")

class ColombianBeans(CoffeeBeans):
    def grind(self):
        print("Mielę ziarna kolumbijskie...")

# Konkretne fabryki
class EspressoMachineFactory(CoffeeMachineFactory):
    def create_coffee(self) -> Coffee:
        return Espresso()

    def create_coffee_beans(self) -> CoffeeBeans:
        return ArabicaBeans()

class LatteMachineFactory(CoffeeMachineFactory):
    def create_coffee(self) -> Coffee:
        return Latte()

    def create_coffee_beans(self) -> CoffeeBeans:
        return RobustaBeans()

class CappuccinoMachineFactory(CoffeeMachineFactory):
    def create_coffee(self) -> Coffee:
        return Cappuccino()

    def create_coffee_beans(self) -> CoffeeBeans:
        return ColombianBeans()

class MochaMachineFactory(CoffeeMachineFactory):
    def create_coffee(self) -> Coffee:
        return Mocha()

    def create_coffee_beans(self) -> CoffeeBeans:
        return ArabicaBeans()

# Klasa fabryki, umożliwiająca wybór rodzaju kawy
class CoffeeMachine:
    def __init__(self):
        self.factory = None

    def choose_factory(self, choice):
        if choice == '1':
            self.factory = EspressoMachineFactory()
        elif choice == '2':
            self.factory = LatteMachineFactory()
        elif choice == '3':
            self.factory = CappuccinoMachineFactory()
        elif choice == '4':
            self.factory = MochaMachineFactory()
        else:
            print("Nieprawidłowy wybór kawy!")

    def make_coffee(self):
        if self.factory is None:
            print("Nie wybrano fabryki. Proszę najpierw wybrać rodzaj kawy.")
            return

        coffee = self.factory.create_coffee() #Tworzenie obiektu kawy
        beans = self.factory.create_coffee_beans() #Tworzenie obiektu ziaren

        beans.grind()
        coffee.brew()
        print("Smacznej kawusi :)")

# Użycie fabryki do wyboru rodzaju kawy
coffee_machine = CoffeeMachine()

choice = input("Wybierz rodzaj kawy (espresso/latte/cappuccino/mocha): ")

if choice == '1':
    coffee_machine.choose_factory(choice)
elif choice == '2':
    coffee_machine.choose_factory(choice)
elif choice == '3':
    coffee_machine.choose_factory(choice)
elif choice == '4':
    coffee_machine.choose_factory(choice)
else:
    print("Nieprawidłowy wybór kawy!")

coffee_machine.make_coffee()
