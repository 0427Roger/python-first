import random
import pyinputplus
print('Guess the number game')
while True:
    min=1
    max=100
    target=random.randint(min,max)
    while True:
        keyin=pyinputplus.inputInt(f'input a number({min}~{max}):',min=min,max=max)
        print(keyin)
        if keyin==target:
            print('Guessed correctly')
            break
        else:
            if keyin<target:
                print('\nBigger')
                min=keyin
            elif keyin>target:
                print('\nSmaller')
                max=keyin
    is_again:str=input('If you want to play again,input "Y",Finish,"N".')
    print(is_again)
    if not is_again=='Y':
        break
print('\nGame over.')