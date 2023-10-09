import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from vispy.color import ColorArray
import fullcontrol as fc
from random import random
from math import tau

import sys

from src.ui.mainwindow import Ui_MainWindow
from generator.test import *

    
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self) #import Qtdesigner
        self.x = np.array([1, 2, 3, 6])
        self.y = np.array([1, 2, 3, 4])
        self.z = np.array([1, 2, 3, 9])
        self.pos = np.c_[self.x, self.y, self.z]
        self.my_plot = self.designer_plot.Plot3D(self.pos, width=1.0, color=ColorArray('#3792cb'), marker_size=0, edge_color='r', symbol="disc", face_color=(0.2, 0.2, 1, 0.8), parent=self.designer_plot.view.scene)
        self.update_button.clicked.connect(self.update)

    # def update(self):
    #     self.xx = np.array([4, 2, 4, 6])
    #     self.yy = np.array([3, 7, 3, 80])
    #     self.zz = np.array([2, 8, 3, 9])
    #     self.pos = np.c_[self.xx, self.yy, self.zz]
    #     self.my_plot.set_data(self.pos)

    def update(self):
        steps = [fc.Point(x=50 * random(), y=50 * random(), z=i * 0.01) for i in range(1000)]
        fc.transform(steps, 'plot')
        gcode_text = fc.transform(steps, 'gcode')
        write_gcode_to_file(gcode_text, 'output.gcode')

        x_coords, y_coords, z_coords = parse_gcode(gcode_text)

        self.xx = np.array(x_coords)
        self.yy = np.array(y_coords)
        self.zz = np.array(z_coords)
        self.pos = np.c_[self.xx, self.yy, self.zz]
        self.my_plot.set_data(self.pos)

        # Print the extracted coordinates
        print("X Coordinates:", x_coords)
        print("Y Coordinates:", y_coords)
        print("Z Coordinates:", z_coords)

if __name__ == "__main__":
    QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling) 
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())