import random
print('Guess the number game.')
def main():
  while True:
    min=1
    max=100
    count=0
    target=random.randint(1,100)
    print(target)
    while True:
      try:
        count+=1
        keyin:int=int(input(f'input namber({min}~{max}):'))
        if keyin<=min or keyin>=max:
          print('input range error.')
          continue
      except:
        print('input format error.')
        continue
      if keyin<target:
        print('Bigger')
        min=keyin
        continue
      elif keyin>target:
        print('Smallier')
        max=keyin
        continue
      elif keyin==target:
        print('Guessed correctly.')
        print(f'Use {count} round.')
        break
    while True:
      print('again(Y,N):')
      is_again=input('again(Y,N):')
      if is_again=='Y' or is_again=='N':
        break
      else:
        print('input format error.')
        continue
    if is_again=='N':
      print('Goodbye!')
      break
    elif is_again=='Y':
      print('again')
      continue
if __name__=='__main__':
  main()

