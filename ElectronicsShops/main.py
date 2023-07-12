from browsing import BrowseLink
from data import StoreLink
from GUI_ElecStores import Ui_MainWindow

from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def search():
    productName = ui.ProductName.toPlainText()
    if productName.strip() != "":
        updateData()  # To update directly when changing the checking
        BrowseLink(productName, link.getData()).beginSearch()


def startCheckingBox():
    # To auto check or uncheck w.r.t. json file
    for i in range(16):
        store: dict = link.getData()["Stores"][i]
        exec(f"ui.shop_{i + 1}.setChecked(store['search'])")


def updateData():
    # UpdateData in the json file
    for i in range(16):
        store: dict = link.getData()["Stores"][i]
        exec("store['search']=ui.shop_{}.isChecked()".format(i + 1))
        link.updateData()


if __name__ == "__main__":
    link = StoreLink()
    startCheckingBox()
    ui.BT_Search.clicked.connect(search)

    sys.exit(app.exec_())
