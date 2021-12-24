# *args: Argumentos de comprimento variável posicional
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(3, 5, 6, 2, 1, 7, 4, 3))

# **kwargs: Argumentos de comprimento variável com palavra-chave
def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)

    calculate(2, add=3, multiply=5)

# How to use a** dicionário kwargs com segurança
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

    # my_car = Car(make="Nissan", model="Skyline")
    #     print(my_car.model)

