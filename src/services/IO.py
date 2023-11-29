from pybtex.database import parse_string

class KonsoliIO():
    def read_input(self, text):
        return input(text)

    def write_screen(self, text):
        print(text)

    def print_readable_form(self,text):
        for i in text:
            type = i.docutype
            if type == "article":
                print("Article", (i.citekey))
                print("- Author:", i.bibDict["author"])
                print("- Title:", i.bibDict["title"])
                print("- Journal:", i.bibDict["journal"])
                print("- Year:", i.bibDict["year"])
                print(" ")
            
            if type == "book":
                print("Book", i.citekey)
                print("- Author:", i.bibDict["author"])
                print("- Editor:", i.bibDict["editor"])
                print("- Title:", i.bibDict["title"])
                print("- Publisher:",  i.bibDict["publisher"])
                print("- Year:", i.bibDict["year"])
                print(" ")
