from services.IO import KonsoliIO
from UI.ui import UI


def main():
    ui = UI(KonsoliIO())
    ui.start()


if __name__ == "__main__":
    main()
