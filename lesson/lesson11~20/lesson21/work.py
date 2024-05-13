import pandas as pd
import requests
import os
from pprint import pprint

def pathData_to_DataFrame(path):
    pathNames=os.listdir(path)
    abspath=[]
    abspath.extend(os.path.abspath(f'{path}/{pathName}') for pathName in pathNames)
    df1=pd.concat(pd.read_csv(path) for path in abspath)
    return df1

def getData_json(url):
    response=requests.get(url)
    try:
        response.raise_for_status()
        if response.status_code==200:
            data=response.json()
            return data
    except Exception as e:
        print(f'ERROR{e}')         
        return None
url='https://ods.railway.gov.tw/tra-ods-web/ods/download/dataResource/0518b833e8964d53bfea3f7691aea0ee'
path='Number of people entering and exiting each station every day'


df1=pathData_to_DataFrame(path)
df1['trnOpDate']=pd.to_datetime(df1['trnOpDate'].astype('str'))
df1=(df1.sort_values(by='trnOpDate'))
df1.groupby(by='staCode')
print(df1)

# data=getData_json(url)
# pprint(data)