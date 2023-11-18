class Bibtex():
    def __init__(self, docutype, citekey):
        self.docutype = docutype
        self.citekey = citekey
        self.bibDict = {
}
    def __str__(self):
        looped = self.loop_to_string()
        return(
            f"@{self.docutype}{{{self.citekey}"
            f"{looped}"
            f"\n}}"
        )
    def loop_to_string(self):
        ret = ""
        for key, value in self.bibDict.items():
            not_year = (key != "year")
            if not_year:
                ret += f",\n    {key} = \"{value}\""
            else:
                ret += f",\n    {key} = {value}"
        if ret == "":
            return ","
        return ret

    def add(self, key, value):
        self.bibDict[key] = value

