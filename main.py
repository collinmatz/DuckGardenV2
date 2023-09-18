from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()