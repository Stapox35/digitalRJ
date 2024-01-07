class Kurs:

    def __init__(self, kursowanie, godziny, szkolny=False):
        self.kursowanie = kursowanie
        self.godziny = godziny
        self.szkolny = szkolny

    def __str__(self):
        s = ""
        s += "KE "+self.kursowanie+"\n"
        s += "GY "+self.godziny + '\n'
        s += "SY "+self.szkolny+'\n'
    