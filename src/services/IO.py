class KonsoliIO():
    def read_input(self, text):
        return input(text)

    def write_screen(self, text):
        print(text)

    def print_readable_form(self,text):
        if not text:
            print("\nYou do not have any refences to print!\n")

        for i in text:
            type = i.docutype

            #TODO: mandatory fields
            if type == "article":
                print("\nArticle, citekey:", (i.citekey))
                print("- Author:", i.bibDict["author"])
                print("- Title:", i.bibDict["title"])
                print("- Journal:", i.bibDict["journal"])
                print("- Year:", i.bibDict["year"])
            
            if type == "book":
                print("\nBook, citekey:", (i.citekey))
                print("- Author:", i.bibDict["author"])
                print("- Editor:", i.bibDict["editor"])
                print("- Title:", i.bibDict["title"])
                print("- Publisher:",  i.bibDict["publisher"])
                print("- Year:", i.bibDict["year"])
