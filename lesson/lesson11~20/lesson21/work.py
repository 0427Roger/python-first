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

path='Number of people entering and exiting each station every day'


df1=pathData_to_DataFrame(path)
df1['trnOpDate']=pd.to_datetime(df1['trnOpDate'].astype('str'))
df1['trnOpDate']=df1.sort_values(by='trnOpDate')
print(df1)