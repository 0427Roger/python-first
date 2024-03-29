from tools import get_names,get_scores
from pprint import pprint
import pyinputplus
import csv
def main():
    nums:int=pyinputplus.inputInt('input one number:',min=1,max=50)
    names:list=get_names(nums)
    scores:list[dict]=get_scores(names)
    with(open('class.csv',mode='w',encoding='utf-8',newline=''))as(file):
        dictwriter=csv.DictWriter(file,fieldnames=['name','nature','history','physics'])
        dictwriter.writeheader()
        dictwriter.writerows(scores)
if __name__=='__main__':
    main()