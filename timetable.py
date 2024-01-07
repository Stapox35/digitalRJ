class Timetable:

    def __init__(self, name):
        
        self.name = name
        self.stacje = []
        self.kursy = []


    def dodajKurs(self, kurs):
        self.kursy.append(kurs)
    
    def dodajStacje(self, stacje):
        self.stacje = stacje

    def iloscStacji(self):
        return len(self.stacje)

    def zapiszRozklad(self, path):
        with open(path+"/"+self.name+".data", 'w') as fileOut:
            fileOut.write(self.name+'\n')
            fileOut.write(str(self.stacje)+'\n')
            fileOut.write("---K\n") # kursy below
            for kurs in self.kursy:
                fileOut.write(str(kurs)+'\n')
            