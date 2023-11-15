from bibtex import Bibtex
from app_logic import AppLogic

class KonsoliIO:
    def __init__(self):
        self.app = AppLogic()

    def add_article(self):
        code = input("Citekey: ")
        bibtex = Bibtex("article", code)

        author = input("Author: ")
        bibtex.add("author", author)

        title = input("Title: ")
        bibtex.add("title", title)

        journal = input("Journal: ")
        bibtex.add("journal", journal)

        year = input("Year: ")
        bibtex.add("year", year)

        self.app.add(bibtex)
        
    
    def add_book(self):
        pass

    def add_inproceeding(self):
        pass

    def print(self, teksti):
        pass
        #Tästä pääsee Print


class UI:
    def __init__(self, io):
        self.io = io

    def start(self):
        while True:
            option = int(input("Choose 1 to add references or choose 2 to print references: "))

            if option == 1:
                form = int(input("1: Article, 2: Book:, 3: inproceeding"))
                if form == 1:
                    self.io.add_article()
                elif form == 2:
                    pass
                
                elif form == 3:
                    pass

            elif option == 2:
                print("kaksi")

            else:
                print("invalid")

def main():
    io = KonsoliIO()
    ui = UI(io)

    ui.start()

main()


        

        

        
            