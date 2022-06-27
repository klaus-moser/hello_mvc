from view_qt import Ui_MainWindow
from PyQt5 import QtWidgets as qtw


class View(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = View()
    widget.show()
    app.exec_()
