from homeworkoop5.model.Animal import Animal
from homeworkoop5.model.Bird import Bird
from homeworkoop5.model.Dog import Dog
from homeworkoop5.model.Fish import Fish

if __name__ == '__main__':
    animal = Animal('Milo', 15, 'Female', 6.3)
    animal.print_animal()
    animal.makes_sound()
    animal.moves()

    dog = Dog('Akita', 2, 'female', 45, 'Akita', 0.5, 'loud')
    dog.print_animal()
    dog.makes_sound()
    dog.moves()

    bird = Bird('Packo', 5, 'Male', 0.6, 'Jako', 0.5, '0.05')
    bird.print_animal()
    bird.makes_sound()
    bird.moves()

    fish = Fish('Vin Diesel', 1, 'Male', 0.01, 'Betta', 500, 'blue')
    fish.print_animal()
    fish.makes_sound()
    fish.moves()

