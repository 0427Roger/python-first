import random
def play_game():
  print('Guess the number game.')
  while True:
    min=1
    max=100
    target=random.randint(1,100)
    while True:
      try:
        keyin=int(input(f'input namber(min~max):'))
        if keyin<=min or keyin>=max:
          print('input error.')
          
      except:
        continue
      if keyin<=target:
        min=keyin
      elif keyin>=target:
        max
    
