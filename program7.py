
# import actors
from actors import Wizard, Creature
import random
import time



def main():
    print_header()
    game_loop()


def print_header():
    print('************************')
    print(' WIZARD GAME APP ')
    print('************************')


def game_loop():
    creatures = [
        Creature('Todaa', 1),
        Creature('Tiger' , 12),
        Creature('Bat' , 3),
        Creature('Draggon' , 50),
        Creature('Evil Wizard', 1000)

    ]
    # print(creatures)
    hero = Wizard('Gandeoof', 75)


    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared  from a forest....'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack. [r]unaway, or [l]ook around ? ')
        if cmd =='a':
           if hero.attack(active_creature):
               creatures.remove(active_creature)
           else:
               print("The wizard runs and hides for recovery ")
               time.sleep(5)
               print("The wizard Returns ")

        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print("The Wizard {} takes in the surroundings and sees: "
                  .format(hero.name))
            for c in creatures:
                print(" * A {} of level {}".format(c.name, c.level))
        else:
            print('OK, existing the game')
            break

        print()

if __name__=='__main__':
    main()
