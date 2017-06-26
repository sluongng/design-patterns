import abc

class Director:

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()
        self._builder._build_part_c()

class Builder(metaclass=abc.ABCMeta):

    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def _build_part_a(self):
        pass
    @abc.abstractmethod
    def _build_part_b(self):
        pass
    @abc.abstractmethod
    def _build_part_c(self):
        pass

class ConcreteBuilder(Builder):

    def _build_part_a(self):
        pass
    def _build_part_b(self):
        pass
    def _build_part_c(self):
        pass

class Product:
    pass

def main():
    concrete_builder = ConcreteBuilder()
    director = Director()
    director.construct(concrete_builder)
    product = concrete_builder.product

if __name__ == "__main__":
    main()
