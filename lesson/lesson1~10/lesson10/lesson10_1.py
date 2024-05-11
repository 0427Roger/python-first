from lesson_tools.my_tools import create_profile,Items
def main():
    items:Items = Items.model_validate(create_profile())
    items.showAll()
if __name__=='__main__':
    main()