class animals:
    animal_list = dict()

    @staticmethod
    def added_animal(name, weight):
        animals.animal_list[name] = weight

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.added_animal(name, weight)

    def feed(self):
        print(f"I'm {self.name}. Good! I am full!")

    def clean_up(self):
        print('Fine! I am clean!')

    def animal_sound(self, sound):
        old_str = "'>"
        print(f"{sound}! This is sound of {str(type(self)).replace(old_str, '')[17:]} {self.name}\n")


class goose(animals):
    def laid_egg(self):
        print(f'I am goose {self.name}. It is a my goose eggs.')


class cow(animals):
    def to_milk(self):
        print('Milk a cow.')


class sheep(animals):
    def shear(self):
        print('Get sheep wool.')


class chicken(animals):
    def laid_egg(self):
        print('It is a chicken eggs.')


class goat(animals):
    def to_milk(self):
        print('Milk a goat.')

    def shear(self):
        print('Get goat wool.')


class duck(animals):
    def laid_egg(self):
        print('It is a duck eggs.')


Goose1 = goose('Gray', 9)

Goose2 = goose('White', 11)

Cow1 = cow('Buryonka', 110)

Sheep1 = sheep('Lamb', 30)

Sheep2 = sheep('Curly', 32)

Chicken1 = chicken('Co-co', 5)

Chicken2 = chicken('Kukareku', 4)

Goat1 = goat('Horns', 18)

Goat2 = goat('Hooves', 16)

Duck1 = duck('Kryakva', 4)

Goose1.laid_egg()
Goose1.clean_up()
Goose1.animal_sound('G-g-g-g-g')

Goose2.laid_egg()
Goose2.animal_sound('Ga-ga-ga')

Cow1.to_milk()
Cow1.animal_sound('Muuuuuu')

Sheep1.shear()
Sheep1.animal_sound('Be-e-e-e-e-e')

Sheep2.shear()
Sheep2.feed()
Sheep2.animal_sound('Be-be-be-be')

Chicken1.laid_egg()
Chicken1.animal_sound('Cocococo')

Chicken2.clean_up()
Chicken2.laid_egg()
Chicken2.animal_sound('Ku-ka-re-ku')

Goat1.shear()
Goat1.to_milk()
Goat1.animal_sound('Me-e-e-e-e-e-e-e')

Goat2.shear()
Goat2.to_milk()
Goat2.animal_sound('Me-me-me-me-me-me')

Duck1.laid_egg()
Duck1.feed()
Duck1.animal_sound('quack-quack')

total_weight = 0
max_weight = ['', 0]
for animal in animals.animal_list:
    total_weight += animals.animal_list[animal]
    if animals.animal_list[animal] > max_weight[1]:
        max_weight[1] = animals.animal_list[animal]
        max_weight[0] = animal
print(f'The total weight of the farm animals is {total_weight} kg')
print(f'{max_weight[0]} has the maximum weight from the farm animals and its weight is {max_weight[1]} kg')
