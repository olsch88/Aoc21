import sys
import numpy as np
import matplotlib as mpl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import PyQt5.QtCore
from threading import Thread
import time
from PyQt5.QtWidgets import (QApplication, QPushButton, QWidget,
                            QVBoxLayout,
                            )


### This is not really finished, but works ;)

class Day11_Animation(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.title = 'Dumbo Octoplus'
        self.left = 100
        self.top = 100        
        self.width = 800
        self.height = 600
        self.data = Puzzel_11()
        
        self.init_ui()        

        self.ini_canvas(self.data.data)

        self.dirs = [np.array([-1,-1]),
                    np.array([0,-1]),
                    np.array([1,-1]),
                    np.array([-1,0]),
                    np.array([-1, 1]),
                    np.array([1,1]), 
                    np.array([1,0]),
                    np.array([0,1])]
        
        self.runnig = False

    def init_ui(self) -> None:
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self._mainlayout = QVBoxLayout()
        self.canvas = PlotCanvas()

        self.start_stop_button = QPushButton("Start Animation")
        self.start_stop_button.clicked.connect(self.btn_clicked)

        self.data.sig_data_updated.connect(self.update_canvas)

        self._mainlayout.addWidget(self.canvas)
        self._mainlayout.addWidget(self.start_stop_button)
        self.setLayout(self._mainlayout)
        self.show()

    
    def ini_canvas(self, data):
        self.canvas.ini_plot(data)

    def update_canvas(self):
        self.canvas.update_plot(self.data.data+1, self.data.count, self.data.sub_count)

    def btn_clicked(self):
        self.runnig = True
        self.start_stop_button.setText("Stop")
        self.run_puzzle()
    
    def run_puzzle(self):
        print("Hello")
        self.data.run_simulation()

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, data=None, width=50, height=40, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.add_subplot(111)
        self.x=[]
        self.y=[]
    def ini_plot(self, data):
        pos = np.argwhere(data)
        self.x = [p[1]for p in pos]
        self.y = [p[0]for p in pos]
        values = data.ravel()
        
        self.axes.scatter(self.x, self.y, values)     
        self.axes.set_title("Dumbo Octoplus Step 0, Substep 0")
        self.show()

    def update_plot(self, data, count, subcount):
        self.axes.clear()
        pos = np.argwhere(data>=0)
        self.x = [p[1]for p in pos]
        self.y = [p[0]for p in pos]
        values = data.ravel()       
        
        self.axes.scatter(self.x, self.y, s=[v**2 for v in values]) 
        self.axes.set_title("Dumbo Octoplus Step {}, Substep {}".format(count, subcount))
        self.draw()

class Puzzel_11(PyQt5.QtCore.QObject):
    sig_data_updated = PyQt5.QtCore.pyqtSignal()

    def __init__(self) -> None:
        PyQt5.QtCore.QObject.__init__(self)
        self.load_data()
        
        self.dirs = [np.array([-1,-1]),
                np.array([0,-1]),
                np.array([1,-1]),
                np.array([-1,0]),
                np.array([-1, 1]),
                np.array([1,1]), 
                np.array([1,0]),
                np.array([0,1])]

        self.has_flashed = np.full(self.data.shape, False)
        self.flash_count = 0
        self.count = 0

    def load_data(self):
        with open("11_input.txt", "r") as file:
            data_raw = file.readlines()
        self.data = np.array([[int (c) for c in line.strip()]for line in data_raw])

    def flash(self, grid, r, c):        
        self.flash_count += 1
        grid[r,c] = 0
        self.has_flashed[r,c]= True
        for pos in self.dirs:
            if 0 <= pos[0]+r <10 and 0 <= pos[1]+c <10: # avoiding the edges
                grid[pos[0]+r, pos[1]+c] += 1

    def scan_flash(self, grid: np.ndarray):
        # I think, that there is an easier way to do this with numpy
        for r in range(grid.shape[0]):
            for c in range(grid.shape[1]):
                if grid[r,c] >= 10:
                    self.flash(grid,r,c)
        self.sig_data_updated.emit()
        time.sleep(.25)

    def update(self): # , grid: np.ndarray=data, count=0):
        while(True):
            self.count += 1
            #has_flashed = np.full(self.data.shape, False)
            self.data = self.data + 1    
            self.sub_count = 0    
            while(np.any(self.data>=10)):
                self.scan_flash(self.data)
                self.sub_count += 1
            if np.all(self.has_flashed):
                print("Step: {}".format(self.count+1))
                return
            self.sig_data_updated.emit()
            time.sleep(.5)
            self.data = np.where(self.has_flashed, 0, self.data)
            self.has_flashed = np.full(self.data.shape, False)

    def run_simulation(self):
        th = Thread(target=self.update)
        th.start()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Day11_Animation()
    sys.exit(app.exec_())
