from Menu import Menu
from vsimple import Environment

if __name__ == "__main__":
    Environment.__module__ = "vsimple"
    menu = Menu()
    menu.run()

