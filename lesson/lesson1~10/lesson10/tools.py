import random
def get_names(nums:int=5)->str:
    with(open('names.txt',encoding='utf-8'))as(file):
        content:list[str]=(file.read()).split('\n')
        random_names=random.choices(content,k=nums)
        return random_names
def get_scores(names:list[str])->list[dict]:
    items:list[dict]=[]
    for name in names:
        item:dict[str:any]={}
        item['name']=name
        item['nature']=random.randint(50,100)
        item['history']=random.randint(50,100)
        item['physics']=random.randint(50,100)
        items.append(item)
    return items