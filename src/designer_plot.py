from vispy import visuals, scene
from vispy.color import ColorArray
from PyQt5.QtWidgets import*
import numpy as np


class Designer_plot(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.canvas = scene.SceneCanvas(parent=self,keys='interactive', title='plot3d', show=True, bgcolor = ColorArray('black'))

        # Add a ViewBox to let the user zoom/rotate
        self.view = self.canvas.central_widget.add_view()
        self.grid = scene.visuals.GridLines(parent=self.view.scene, scale=(1, 1))
        self.view.camera = 'turntable'
        self.view.camera.fov = 25
        self.view.camera.distance = 60
        # plot
        self.Plot3D = scene.visuals.create_visual_node(visuals.LinePlotVisual)
