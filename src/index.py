from services.IO import ConsoleIO
from UI.ui import UI


def main():
    ui = UI(ConsoleIO())
    ui.start()


if __name__ == "__main__":
    main()
