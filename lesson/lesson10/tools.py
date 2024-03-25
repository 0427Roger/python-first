from pydantic import BaseModel,RootModel
import random
def create_profile()->list[dict]:
    data=[]
    name:str=['Roger','Zhijia','Emma']
    height:float=[random.randint(140,200)for _ in name]
    weight:float=[random.randint(30,100)for _ in name]
    for i in range(len(name)):
        person_item=[{'name':name[i],'height':height[i],'weight':weight[i]}]
        data.extend(person_item)
    return data
class Item(BaseModel):
    name:str
    height:float
    weight:float
    def show(self):
        print(f'Name:{self.name},BMI={self.bmi :.2f},{self.judge}')
    @property
    def bmi(self)->float:
        return self.weight/(self.height/100)**2
    @property
    def judge(self)->str:
        if self.bmi<18.5:
            return 'underweight'
        elif self.bmi<24:
            return 'normal weight'
        elif self.bmi<27:
            return 'over weight'
        elif self.bmi<30:
            return 'mild obesity'
        elif self.bmi<35:
            return 'moderately obese'
        else:
            return 'severe obesity'
class Items(RootModel):
    root:list[Item]
    
    def showAll(self):
        for item in self.root:
            item.show() 
    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]