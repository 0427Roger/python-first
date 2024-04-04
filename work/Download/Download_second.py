import requests
from requests import Response
from pydantic import RootModel,BaseModel,Field
import pandas as pd



def get_Taipei_youbike()->Response|None:
    Taipei_youbike_url='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response:Response=requests.get(Taipei_youbike_url)
    try:
        response.raise_for_status()
        if response.status_code==200:
            print('Download successful.')
            return response
        else:
            print('Status code error.')
            print('Download failed.')
            return None
    except Exception as e:
        print(f'HTTP error occurred:{e}')
        return None

class Site(BaseModel):
    站點名稱:str=Field(alias='sna')
    總借車輛:int=Field(alias='tot')
    可借:int=Field(alias='sbi')
    行政區:str=Field(alias='sarea')
    時間:str=Field(alias='mday')
    可還:int=Field(alias='bemp')

class Sites(RootModel):
    root:list[Site]

def main():
    response:Response=get_Taipei_youbike()
    if response:
        rawString:str=response.text
    data:list[dict]=Sites.model_validate_json(rawString)
    return display(pd.DataFrame(data))
if __name__=='__main__':
    main()