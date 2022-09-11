# VisPy test 
This repository is a test for updating vispy plot via a push button. The UI has been made with the help of QT designer
## Success init
self.x = np.array([1, 2, 3, 6])  
self.y = np.array([1, 2, 3, 4])  
self.z = np.array([1, 2, 3, 9])  
self.pos = np.c_[self.x, self.y, self.z]  
self.designer_plot.Plot3D(self.pos, width=8.0, color=ColorArray('#3792cb'), marker_size=0, edge_color='r', symbol="disc", face_color=(0.2, 0.2, 1, 0.8), parent=self.designer_plot.view.scene)  
Initial data is loaded succesfully in startup  
<img align="center" src="https://github.com/PanagiotisMenounos/visPy_test/blob/main/img/init.PNG" />

# Fail to update  
When Update push button is presseed, self.designer_plot.Plot3D.set_data(self.pos) in main.py fails to set the new data  
<img align="center" src="https://github.com/PanagiotisMenounos/visPy_test/blob/main/img/fail.PNG" />