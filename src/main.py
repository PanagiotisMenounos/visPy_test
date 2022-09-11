import cv2
import sys
import serial.tools.list_ports
import time
import os
import easygui
import socket
import numpy as np
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QInputDialog, QLineEdit
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from matplotlib import pyplot
from vispy.color import ColorArray

import sys
from vispy import app, visuals, scene

from mainwindow import Ui_MainWindow

    
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self) #import Qtdesigner
        self.x = np.array([1, 2, 3, 6])
        self.y = np.array([1, 2, 3, 4])
        self.z = np.array([1, 2, 3, 9])
        self.pos = np.c_[self.x, self.y, self.z]
        self.designer_plot.Plot3D(self.pos, width=8.0, color=ColorArray('#3792cb'), marker_size=0, edge_color='r', symbol="disc", face_color=(0.2, 0.2, 1, 0.8), parent=self.designer_plot.view.scene)
        self.update_button.clicked.connect(self.update)

    def update(self):
        self.xx = np.array([4, 2, 4, 6])
        self.yy = np.array([3, 7, 3, 80])
        self.zz = np.array([2, 8, 3, 9])
        self.pos = np.c_[self.xx, self.yy, self.zz]
        self.designer_plot.Plot3D.set_data(self.pos)

if __name__ == "__main__":
    QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling) 
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())