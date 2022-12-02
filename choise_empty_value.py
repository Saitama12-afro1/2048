import random


def choise_empty_value(array, choise1 = 0, choise2 = 0):
    if not choise1:
        choise1 = random.randint(0, 15)
    if not choise2:
        choise2 = random.randint(0, 15)
    if choise1 == choise2:
        while choise1 == choise2:
            choise2 = random.randint(0, 15)
    if not array[choise1] and  not array[choise2]:
        choise_empty_value(array)
    elif array[choise1] and not array[choise2]:
        choise_empty_value(array, choise1 = choise1)
    elif not array[choise1] and array[choise2]:
        choise_empty_value(array,  choise2 = choise2)
            
    return choise1, choise2

a = [1,4,6, None, 53, 61, None, 53, 32, 0, 1, None, 1, None, 32,14]
