
# import actors
from actors import Wizard, Creature

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
    print(creatures)
    hero = Wizard('Gandeoof', 75)


    while True:

        cmd = input('Do you [a]ttack. [r]unaway, or [l]ook around ? ')
        if cmd =='a':
            print('attack')
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('look around')
        else:
            print('OK, existing the game')
            break

if __name__=='__main__':
    main()
