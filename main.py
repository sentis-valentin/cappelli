import sys

from PyQt5.QtWidgets import *

from PyQt5.QtWebEngineWidgets import *

from PyQt5.QtCore import *

class Window(QMainWindow):

   
    def __init__(self):
       
        super(Window,self).__init__()

        
        self.browser = QWebEngineView()

        
        self.browser.setUrl(QUrl('https://sentis-valentin.github.io/cappelli/'))

        
        self.setCentralWidget(self.browser)

        
        self.showMaximized()

        
        self.browser.urlChanged.connect(self.updateUrl)

    
    def home(self):
        self.browser.setUrl(QUrl('https://sentis-valentin.github.io/cappelli/'))

   
    def loadUrl(self):
        
        url = self.searchBar.text()
        
        self.browser.setUrl(QUrl(url))

    
    def updateUrl(self, url):
        
        self.searchBar.setText(url.toString())


MyApp = QApplication(sys.argv)


QApplication.setApplicationName('Cappelli')


window = Window()


MyApp.exec_()

# pip install PyQtWebEngine
# pip install PyQt5
