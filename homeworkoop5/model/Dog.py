from overrides import overrides

from homeworkoop5.model.Animal import Animal


class Dog(Animal):
    def __init__(self, name, age, gender, weight, breed, tail_length, bark_volume ):
        super().__init__(name, age, gender, weight)
        self.breed = breed
        self.tail_length = tail_length
        self.bark_volume = bark_volume

    @overrides
    def makes_sound(self):
        print('Woof!')

    @overrides
    def moves(self):
        print('Im running')


