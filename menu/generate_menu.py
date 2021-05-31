from menu.menu_route import menu_dict
from menu.models import Menu, MenuList, MenuView


def generate_menu(menu_dict: dict, parent=None) -> Menu:
    if "children" in menu_dict:
        menu = MenuList(menu_dict["name"], parent, description=menu_dict["description"])
        for child in menu_dict["children"]:
            generate_menu(child, parent=menu)
    elif "function" in menu_dict:
        menu = MenuView(menu_dict["name"], function=menu_dict["function"], parent=parent,
                        description=menu_dict["description"])
    else:
        raise Exception("wrong")
    return menu


# print(menu_dict)
main_menu = generate_menu(menu_dict=menu_dict)
