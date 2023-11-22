from IO import UI
from IO import KonsoliIO

def main():
    ui = UI(KonsoliIO())
    ui.start()

if __name__ == "__main__":
    main()