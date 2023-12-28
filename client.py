from src.client.main_widgets.main_window import MainWindow
from PySide6 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    root = MainWindow()
    app.exec()
    

