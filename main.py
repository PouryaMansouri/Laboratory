from menu.models import MenuList

main_menu = MenuList("Laboratory Main Menu", description="Group 3 project")
register_menu = MenuList("Registration", parent=main_menu,)
Test_menu = MenuList("Test", parent=main_menu,)


main_menu()
