import random
import pandas as pd
import csv
from io import StringIO
import requests
from requests import Response

def get_names(num:int=5)->list[str]:
    with open('names.txt',encoding='utf-8') as file:
        context=file.read().split('\n')
        names:str=random.choices(context,k=num)
        return names

def get_physical(names)->list[dict[str,int,int]]:
    items:list=[]
    for name in names:
        item:dict={}
        item['name']:str=name
        item['height']:int=random.randint(150,200)
        item['weight']:int=random.randint(50,80)
        items.append(item)
    return items

def download(url)->Response|None:
    response:Response=requests.get(url)
    try:
        response.raise_for_status()
        if response.status_code==200:
            print('download successful')
            return response
    except Exception as e:
        print(f'Error:{e}')
        return None