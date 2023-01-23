from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QSpinBox, QFormLayout
from PyQt6.QtGui import QIcon
import sys  

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.Test()

    def Test(self):
        self.setWindowTitle('Layout')
        self.resize(800,800)
        name = QLineEdit()
        password = QLineEdit()
        email = QLineEdit()
        age_spinbox = QSpinBox()

        password.setEchoMode(QLineEdit.EchoMode.Password)
        formLayout = QFormLayout()
        formLayout.addRow('Name:', name)
        
        formLayout.addRow('email:', email)
        formLayout.addRow('age:', age_spinbox)
       
       

        self.setLayout(formLayout)
        self.show()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(qApp.exec())