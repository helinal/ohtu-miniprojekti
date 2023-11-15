class Bibtex():
    def __init__(self, docutype, citekey):
        self.docutype = docutype
        self.citekey = citekey
        self.bibDict = {
}
    def __str__(self):
        looped = self.loop_to_string()
        return(
            f"@{self.docutype}{{{self.citekey},\n"
            f"{looped}"
            f"}}"
        )
    def loop_to_string(self):
        ret = ""
        for key, value in self.bibDict.items():
            ret += f"    {key} = {value}\n"
        return ret

    def add(self, key, value):
        self.bibDict[key] = value

