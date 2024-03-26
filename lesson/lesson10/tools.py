import random
def get_names(nums:int=5)->list[str]:
    with open('names.txt',encoding='utf-8') as file:
        content:list=file.read()
        names:list[str]=content.split(sep='\n')
        random_names=random.choices(names,k=nums)
        return random_names