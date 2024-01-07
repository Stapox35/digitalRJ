from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys, os

import UIFunctions, timetable

nameOfDir = {"src": "materialy", "temp": "tmp"}

btnList = []
#numberOfFile = -1

class MainWindow(QMainWindow):

    def __init__(self): 
        super().__init__() 
        self.numberOfFile = -1
        self.listOfFile = []
        self.path = ""
        self.timetable = None

        self.setWindowTitle("Digitalizacja rozkładów jazdy PKP PKS ") 
  
        self.setGeometry(100, 100, 600, 400) 
        self.showMaximized() 
        self.initWindow()

        self.UiComponents() 
  
        self.show() 
  
    def UiComponents(self): 
        styleForButton = "border: 0.5px solid white"
        empty = QWidget(self)
        self.setCentralWidget(empty)

        layout1 = QGridLayout()

        layoutLeft = QVBoxLayout()
        layoutDown = QHBoxLayout()
        foo = QWidget()
        foo.setLayout(layoutLeft)
        foo.setMaximumWidth(400)
        layout1.addWidget(foo, 0,0)
        layout1.addLayout(layoutDown, 1,1)

        thisFile = QLabel("Obecny plik: None")
        layoutLeft.addWidget(thisFile)
        listOfStation = QListWidget()
        


        listOfStation.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        layoutLeft.addWidget(listOfStation)

        
        label = QLabel()
        layout1.addWidget(label, 0, 1)

        btnList.append({"name": "&Otwórz folder", "row": 2, "col": 0, "func": self.openFolder, "desc": "", "args": [thisFile, label]})
        btnList.append({"name": "&Utwórz nowy rozkład", "row": 3, "col": 0, "func": self.newTimetable, "desc": "", "args": None})
        btnList.append({"name": "&Definiuj stacje", "row": 4, "col": 0, "func": None, "desc": "", "args": None})
        btnList.append({"name": "Dodaj &kurs", "row": 5, "col": 0, "func": None, "desc": "", "args": None})
        btnList.append({"name": "P&odejrzyj wpisane kurs", "row": 6, "col": 1, "func": None, "desc": "", "args": None})     
        btnList.append({"name": " < ", "row": 6, "col": 3, "func": self.imageRight, "desc": "", "args": [label, -1, thisFile]})   
        btnList.append({"name": " > ", "row": 6, "col": 2, "func": self.imageRight, "desc": "", "args": [label, 1, thisFile]})        

        btnList.append({"name": "&Generuj pliki", "row": 6, "col": 4, "func": None, "desc": "", "args": None})           
        btnList.append({"name": "&Zapisz", "row": 6, "col": 0, "func": self.saveTimetable, "desc": "", "args": None})       


        

        for button in btnList:
            btn = QPushButton(button["name"])
            btn.setStyleSheet(styleForButton)
            btn.setMinimumHeight(40)
            if button["func"] != None:
                #btn.clicked.connect(lambda: self.onclick(button["args"]))
                btn.clicked.connect(lambda checked, v=(button["func"], button["args"]): self.onclick(v))
            if button["col"] == 0:
                layoutLeft.addWidget(btn)
            else:
                layoutDown.addWidget(btn)

        empty.setLayout(layout1)



    def onclick(self, args):
        args[0](args[1])
    

    def openFolder(self, listArgs):
        folderpath = QFileDialog.getExistingDirectory(self, 'Wybierz folder')
        self.path = folderpath
        folderpath +="/"+nameOfDir["src"]
        self.listOfFile = sorted(os.listdir(folderpath))
        #FIXME: sprawdzic czy plik to na pewno jpg!! i przygotowac liste na same jpg
        self.numberOfFile = 0
        actualFile = self.listOfFile[self.numberOfFile]
        listArgs[0].setText(actualFile)

        # ---- open image -------
        listArgs[1].setPixmap(UIFunctions.image(folderpath+"/"+actualFile))


    def imageRight(self, listArgs):
        self.numberOfFile = (self.numberOfFile+int(listArgs[1])) % len(self.listOfFile)
        #print(self.path+"/"+nameOfDir["src"] + "/" + self.listOfFile[self.numberOfFile])
        
        listArgs[0].setPixmap(UIFunctions.image(self.path+"/"+nameOfDir["src"] + "/" + self.listOfFile[self.numberOfFile]))
        listArgs[2].setText(self.listOfFile[self.numberOfFile])

    def initWindow(self):
        self.setStyleSheet("background-color: black; color: white")

    def newTimetable(self, listArgs):
        text, ok = QInputDialog.getText(self, 'Nazwa rozkładu jazdy', 'Wprowadź oznaczenie rozkładu jazdy')
        if ok == True:
            self.timetable = timetable.Timetable(text)
    
    def saveTimetable(self, listArgs):
        self.timetable.zapiszRozklad(self.path)
