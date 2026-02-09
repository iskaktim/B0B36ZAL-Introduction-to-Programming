STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "

def writeTextToFile(parametr):
    result = STATICKY_TEXT + str(parametr)
    soubor = "output.txt"
    with open (soubor, "w") as vystup:
        vystup.write(result)
        return soubor