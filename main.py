import os
import sys
import random
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, QTimer

from PyQt5.QtWidgets import QWidget, QApplication

class MainForm(QWidget):
    
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "main.ui"), self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_rand_number)
    
        
    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        print("start")
        if not self.timer.isActive():
            self.timer.start(50)
        else:
            print("already start!")
    
    @pyqtSlot()
    def on_pushButton_stop_clicked(self):
        print("stop")
        self.timer.stop()
    
    def show_rand_number(self):
        # print("rand")
        rand_num = random.randint(0, 1000)
        self.label_result.setText(f"{rand_num}")
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())