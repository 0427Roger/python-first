from lesson_tools.tools import create_profile
def main():
    items=Items.model_validate(create_profile())
    items.showAll()
if __name__=='__main__':
    main()