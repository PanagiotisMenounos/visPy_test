import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSizePolicy
from PyQt5.QtWebEngineWidgets import QWebEngineView
import fullcontrol as fc
import lab.fullcontrol as fclab
from random import random

app = QApplication(sys.argv)

class PlotlyWebView(QMainWindow):
    def __init__(self, html_content):
        super().__init__()

        self.setWindowTitle("Plotly in PyQt WebEngine")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        layout = QVBoxLayout()
        self.webview = QWebEngineView()
        layout.addWidget(self.webview)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.webview.setHtml(html_content)

if __name__ == "__main__":


    # outline_edge_1 = fc.circleXY(fc.Point(x=0, y=0, z=0.2), 5, 0, 64)
    # outline_edge_2 = fc.circleXY(fc.Point(x=1, y=0, z=0.2), 3, 0, 64)
    # steps = fclab.convex_pathsXY(outline_edge_1, outline_edge_2, 10)
    # html_content = fc.transform(steps, 'plot', fc.PlotControls(color_type='print_sequence', style='tube'))

    steps = [fc.polar_to_point(centre=fc.Point(x=0, y=0, z=i * 0.005), radius=10, angle=i * 4.321) for i in range(1000)]
    html_content = fc.transform(steps, 'plot')

    # bez_points = []
    # bez_points.append(fc.Point(x=10, y=10, z=0))
    # bez_points.append(fc.Point(x=10, y=0, z=0))
    # bez_points.append(fc.Point(x=0, y=10, z=0))
    # bez_points.append(fc.Point(x=10, y=10, z=0))
    # bez_points.append(fc.Point(x=9, y=9, z=2))
    # steps = fclab.bezierXYdiscrete(bez_points, num_points=100)
    # html_content = fc.transform(steps, 'plot', fc.PlotControls(style="line", zoom=0.8))

    # steps = [fc.Point(x=50 * random(), y=50 * random(), z=i * 0.01) for i in range(1000)]
    # html_content = fc.transform(steps, 'plot')

    window = PlotlyWebView(html_content)
    window.show()

    sys.exit(app.exec_())