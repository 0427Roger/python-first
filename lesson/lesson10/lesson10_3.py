from tools import get_names,get_scores,inputInt
from pprint import pprint
def main():
    pprint(get_scores(get_names(inputInt('input number value:',0,30))))
if __name__=='__main__':
    main()