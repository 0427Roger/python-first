from tools import create_profile
def main():
    items=Items.model_validate(create_profile())
    items.showAll()
main()