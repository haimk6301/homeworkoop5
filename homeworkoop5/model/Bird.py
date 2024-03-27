from overrides import overrides

from homeworkoop5.model.Animal import Animal


class Bird(Animal):
    def __init__(self, name, age, gender, weight, specie, wing_span, beak_length):
        super().__init__(name, age, gender, weight)
        self.specie = specie
        self.wing_span = wing_span
        self.beak_length = beak_length

    @overrides
    def makes_sound(self):
        print('Chirp chirp!')

    @overrides
    def moves(self):
        print(' Im flying')
