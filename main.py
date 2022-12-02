import sys
import random

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QGridLayout, QHBoxLayout
from PyQt6 import QtCore


from choise_empty_value  import choise_empty_value
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # self.label = QLabel()
        # self.input = QLineEdit()
        # self.input.textChanged.connect(self.label.setText)
        main_box = QVBoxLayout(self)
        main_box.addStretch(0)
        layout_1 = QHBoxLayout()
        layout_1.addStretch(0)
        layout_2 = QHBoxLayout()
        layout_2.addStretch(0)
        layout_3 = QHBoxLayout()
        layout_3.addStretch(0)
        layout_4 = QHBoxLayout()
        layout_4.addStretch(0)
        main_box.addLayout(layout_1)
        main_box.addLayout(layout_2)
        main_box.addLayout(layout_3)
        main_box.addLayout(layout_4)
        self.setFixedSize(1000,1000)
        array_buttons = [[],[],[],[]]
        for i in range(16):
            if i <= 3:
                self.button = QPushButton()
                self.button.setFixedSize(50, 50)
                layout_1.addWidget(self.button)
                array_buttons[0].append(self.button) 
            elif i <= 7:
                self.button = QPushButton()
                self.button.setFixedSize(50, 50)
                layout_2.addWidget(self.button)
                array_buttons[1].append(self.button)
            elif i <= 11:
                self.button = QPushButton()
                self.button.setFixedSize(50, 50)
                layout_3.addWidget(self.button)
                array_buttons[2].append(self.button) 
            elif i <= 15:
                self.button = QPushButton()
                self.button.setFixedSize(50, 50)
                layout_4.addWidget(self.button)
                array_buttons[3].append(self.button)
        arr = []
        for i in array_buttons:
            for j in i:
                arr.append(j.text())
        self.arr = arr
        self.array_buttons = array_buttons
        container = QWidget()
        container.setLayout(main_box)
        self.setCentralWidget(container)
    def getArrayButtons(self):
        return self.array_buttons
    
    def getArray(self):
        return self.arr
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_W:
            print(111111)
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()
