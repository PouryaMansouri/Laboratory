from abc import ABC

from core.models import BaseModel


class Node:
    def __init__(self, parent=None) -> None:
        self.children = []
        assert parent is None or isinstance(parent, Node)  # parent must be node
        self.parent = parent
        if parent:
            self.parent.children.append(self)


class Menu(ABC, Node):
    def __init__(self, name, parent=None, description=""):
        Node.__init__(self, parent)  # TODO: use super
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.name}\n{self.description}"


class MenuList(Menu):
    def __call__(self, *args, **kwargs):
        print(f'{self.parent.name} > {self.name}' if self.parent else self.name)
        print(f'{self.description}')
        print("\nMenu items:")
        for id_menu, sub_menu in enumerate(self.children):
            print(f"\t{id_menu+1}.{repr(sub_menu)}",end="")

