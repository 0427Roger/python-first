import random
def play_game():
  print('Guess the number game.')
  while True:
    min=1
    max=100
    target=random.randint(1,100)
    while True:
      try:
        keyin:int=int(input(f'input namber(min~max):'))
        if keyin<=min or keyin>=max:
          print('input range error.')
          continue
      except:
        print('input format error.')
        continue
      if keyin<=target:
        print('Bigger')
        min=keyin
      elif keyin>=target:
        print('smallier')
        max=keyin
      else keyin==target:
        print('Win')
