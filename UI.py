from Finder import find_key
from StringToDIct import string_to_dict

__author__ = 'varg'

import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("finder.ui")[0]


class FinderWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.resultLineEdit.mousePressEvent = lambda _ : self.resultLineEdit.selectAll()
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.finder.returnPressed.connect(self.pushButton_clicked)
        self.finder.textChanged.connect(self.pushButton_clicked)
        self.textEdit.selectionChanged.connect(self.get_selected)

    def get_selected(self):
        cursor = self.textEdit.textCursor()
        selected = cursor.selectedText()
        self.finder.setText(selected)

    def pushButton_clicked(self):
        text = str(self.textEdit.toPlainText())
        data_structure = string_to_dict(text)
        if not data_structure:
            self.resultLineEdit.setText('Incorrect data structure')
            return

        key = str(self.finder.text())
        if not key:
            self.resultLineEdit.setText('Incorrect key structure')
            return

        key_path = find_key(data_structure, key)
        if not key_path:
            self.resultLineEdit.setText('Key not found')
            return

        self.resultLineEdit.setText(key_path)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWindow = FinderWindowClass(None)
    myWindow.show()
    app.exec_()
