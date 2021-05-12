#!/usr/bin/python3
"""
Graphical User Interface for Steganography Application
Author: Sathvik PN
GitHub: https://github.com/SathvikPN
"""

from src import core, utility, custom_exceptions 

from PyQt5 import QtCore, QtGui, QtWidgets


# -----------------------------------------------
class UI_MainWindow():

    # Function to display Message/Error/Information 
    def display_msg(self, title, msg, ico_type=None):
        MsgBox = QtWidgets.QMessageBox()
        MsgBox.setText(msg)
        MsgBox.setWindowTitle(title)

        if ico_type == 'err':
            ico = QtWidgets.QMessageBox.critical
        else:
            ico = QtWidgets.QMessageBox.information

        MsgBox.setIcon(ico)
        MsgBox.exec()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())