import mainWindow
import sys
from PyQt5.QtWidgets import * 

App = QApplication([]) 
  
window = mainWindow.MainWindow() 
  
sys.exit(App.exec()) 
