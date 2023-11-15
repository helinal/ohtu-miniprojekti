class Bibtex():
    def __init__(self, docutype, citekey):
        self.docutype = docutype
        self.citekey = citekey
        self.bibDict = {}
<<<<<<< HEAD
=======
        
>>>>>>> 51dea41 ( first version of IO)
    def __str__(self):
        looped = self.loop_to_string()
        return(
            f"@{self.docutype}\{self.citekey},"
            f"{looped}"
<<<<<<< HEAD
            f"\}"
        )
    def loop_to_string(self):
=======
            f"\"
            )
        
    def loop_to_string():
>>>>>>> 51dea41 ( first version of IO)
        ret = ""
        for x in self.bibDict:
            ret += "\n  "
            ret += x
            ret += " = \""
            ret += bibDict(x)
            ret += "\","

<<<<<<< HEAD
    def add(self, key, value):
=======
    def add(self,key, value):
>>>>>>> 51dea41 ( first version of IO)
        self.bibDict[key] = value