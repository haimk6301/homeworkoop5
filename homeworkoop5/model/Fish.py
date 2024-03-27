from overrides import overrides

from homeworkoop5.model.Animal import Animal


class Fish(Animal):
    def __init__(self, name, age, gender, weight, specie, fin_count, scale_color):
        super().__init__(name, age, gender, weight)
        self.specie = specie
        self.fin_count = fin_count
        self.scale_color = scale_color

    @overrides
    def makes_sound(self):
        super().makes_sound()
        print('‘Fish is not making a sound')

    @overrides
    def moves(self):
        print('Im swimming')