from tools import get_names,get_scores
from pprint import pprint
import pyinputplus
def main():
    pprint(get_scores(get_names(pyinputplus.inputInt('input number value:',min=0,max=30))))
if __name__=='__main__':
    main()