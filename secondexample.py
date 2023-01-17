from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QIcon
import sys  

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.Test()


    def Test(self):
        self.setWindowTitle('Simple example 2')
        self.setWindowIcon(QIcon('240px-Smiley.svg.png'))
        btnClick = QPushButton(parent=self)
        btnClick.setText('Quit')
        btnClick.move(110,50)
        btnClick.clicked.connect(QApplication.instance().quit)
        self.resize(900,900)
        self.show()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())