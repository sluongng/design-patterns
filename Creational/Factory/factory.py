import abc


class Creator(metaclass=abc.ABCMeta):
    def __init__(self):
        self.product = self._factory_method()

    @abc.abstractmethod
    def _factory_method(self):
        pass

    def some_operation(self):
        self.product.interface()


class ConcreteCreator1(Creator):
    def _factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def _factory_method(self):
        return ConcreteProduct2()


class Product(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface(self):
        pass


class ConcreteProduct1(Product):
    def interface(self):
        pass


class ConcreteProduct2(Product):
    def interface(self):
        pass


def main():
    concrete_creator = ConcreteCreator1()
    concrete_creator.product.interface()
    concrete_creator.some_operation()


if __name__ == "__main__":
    main()
