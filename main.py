from PyQt5 import QtWidgets
from components import Database as db
from containers import Main
import sys
# Displaying the timetable
# Entry point for application
if __name__ == '__main__':
#check database
    if not db.checkSetup():
        db.setup()
    app = QtWidgets.QApplication(sys.argv)
    parent = QtWidgets.QMainWindow()
    Main.MainWindow(parent)
    parent.show()
    sys.exit(app.exec_())
    print ("timetable")
    print ("Done")
