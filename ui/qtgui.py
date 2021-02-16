import sys
from PyQt5.QtWidgets import QApplication, QLabel, QToolBar, QWidget, QMainWindow, QAction
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        
        self.setWindowTitle("My Awesome App")

        label = QLabel("This is a PyQt5 window!")

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)
        toolbar = QToolBar("A coolbar, not a toolbar")
        self.addToolBar(toolbar)
        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)
    def onMyToolBarButtonClick(self, s):
            print("click", s)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()