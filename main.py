from controler import Controller
from view import View


def main():
    view = View()
    game = Controller(view)
    game.run()


if __name__ == "__main__":
    main()
