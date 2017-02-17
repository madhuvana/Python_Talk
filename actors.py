import  random

class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print('The wizard {} attacks {}!'.format(
            self.name, creature.name
        ))

        if __name__ == '__main__':
            my_roll=random.randint(1, 12) * self.level
            creature_roll = random.randint(1, 12) * creature.level

            print("You roll {}....".format(my_roll))
            print("{} rolls {}....".format(creature))

            if my_roll >= creature_roll:
                print("The wizzard has handia"
                      "dly triumphped  over {}".format(creature.name))
                return  True
            else:
                print(" The Wizard has been DEFEATED!")
                return  False



class Creature:
    def __init__(self, name, the_level=10):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature:{} of level {}".format(
            self.name, self.level
        )
