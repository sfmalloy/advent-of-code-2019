import os
from io import TextIOWrapper
from intcode import Intcode
from itertools import combinations


HELP_STR = '''
== misc ==
h | help => show this dialog

== moving ==
n | north => move north
e | east => move east
s | south => move south
w | west => move west

== actions ==
t | take <item> => add item from room to inventory
d | drop <item> => remove item from inventory and drop in current room

'''


def main(file: TextIOWrapper):
    comp = Intcode(file.read())
    # autoplay(comp)
    play(comp)


# grabs all useful items and returns to weighted plate area
def get_items(comp: Intcode):
    pre_steps = '\n'.join([
        'north',
        'take candy cane',
        'south',
        'south',
        'take fuel cell',
        'south',
        'take manifold',
        'north',
        'north',
        'west',
        'take mutex',
        'south',
        'south',
        'take coin',
        'west',
        'take dehydrated water',
        'south',
        'take prime number',
        'north',
        'east',
        'north',
        'east',
        'take cake',
        'north',
        'west',
        'south'
    ]) + '\n'
    comp.read_in_ascii(*pre_steps)


def autoplay(comp: Intcode):
    get_items(comp)
    items = [
        'candy cane',
        'fuel cell',
        'manifold',
        'mutex',
        'coin',
        'dehydrated water',
        'prime number',
        'cake'
    ]

    comp.run()
    comp.read_out_ascii()
    print(pick_and_drop(comp, items))


def pick_and_drop(comp: Intcode, items: list[str]):
    for r in range(1, len(items)):
        for dropped in combinations(items, r):
            for item in dropped:
                comp.read_in_ascii(*f'drop {item}\n')
            comp.read_in_ascii(*'west\n')
            comp.run()
            response = comp.read_out_ascii()
            if '== Security Checkpoint ==' not in response:
                return response
            for item in dropped:
                comp.read_in_ascii(*f'take {item}\n')


def play(comp: Intcode):
    while comp.run() != 99:
        print(comp.read_out_ascii())
        ipt = input()
        if not ipt:
            continue
        match ipt.split()[0]:
            case 'reset':
                comp.reset()
                continue
            case 'n'|'N'|'north':
                ipt = 'north'
                clear()
            case 's'|'S'|'south':
                ipt = 'south'
                clear()
            case 'e'|'E'|'east':
                ipt = 'east'
                clear()
            case 'w'|'W'|'west':
                ipt = 'west'
                clear()
            case 't'|'T'|'take':
                ipt = ' '.join(['take', *ipt.split()[1:]])
            case 'd'|'D'|'drop':
                ipt = ' '.join(['drop', *ipt.split()[1:]])
            case 'h'|'H'|'help':
                print(HELP_STR)
                continue
            case 'q'|'Q'|'quit':
                confirm = input('Are you sure you want to quit? (y/N)')
                if confirm.lower() == 'y':
                    return
                continue
            
        comp.read_in_ascii(*f'{ipt}\n')
    print(comp.read_out_ascii())


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

