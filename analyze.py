
from pyqtgraph.flowchart import Flowchart, Node
from pyqtgraph.flowchart.library.common import CtrlNode
import pyqtgraph.flowchart.library as fclib
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
from DIPPID_pyqtnode import BufferNode, DIPPIDNode
from pyqtgraph_Nodes import  LogNode


if __name__ == '__main__':
    print("la")
    app = QtGui.QApplication([])
    win = QtGui.QMainWindow()
    win.setWindowTitle('Analyze DIPPID DATA')
    cw = QtGui.QWidget()
    win.setCentralWidget(cw)
    layout = QtGui.QGridLayout()
    cw.setLayout(layout)

    # setup layout
    fc = Flowchart(terminals={})
    w = fc.widget()
    layout.addWidget(fc.widget(), 0, 0, 2, 1)
    pwX = pg.PlotWidget()
    pwY = pg.PlotWidget()
    pwZ = pg.PlotWidget()
    layout.addWidget(pwX, 0, 1)
    layout.addWidget(pwY, 0, 2)
    layout.addWidget(pwZ, 1, 1)
    pwX.setYRange(0, 2)
    pwY.setYRange(0, 2)
    pwZ.setYRange(0, 2)

    # setup flowchart nodes
    dippidNode = fc.createNode("DIPPID", pos=(0, 0))
    bufferNodeX = fc.createNode("Buffer", pos=(150, -100))
    pwNodeX = fc.createNode('PlotWidget', pos=(300, -100))
    pwNodeX.setPlot(pwX)
    bufferNodeY = fc.createNode("Buffer", pos=(150, 0))
    pwNodeY = fc.createNode('PlotWidget', pos=(300, 0))
    pwNodeY.setPlot(pwY)
    bufferNodeZ = fc.createNode("Buffer", pos=(150, 100))
    pwNodeZ = fc.createNode('PlotWidget', pos=(300, 100))
    pwNodeZ.setPlot(pwZ)
    logNode = fc.createNode("Log", pos=(450, 0))


    # setup node connections

    fc.connectTerminals(bufferNodeX['dataOut'], logNode['dataIn'])

    fc.connectTerminals(dippidNode['accelX'], bufferNodeX['dataIn'])
    fc.connectTerminals(dippidNode['accelY'], bufferNodeY['dataIn'])
    fc.connectTerminals(dippidNode['accelZ'], bufferNodeZ['dataIn'])
    fc.connectTerminals(bufferNodeX['dataOut'], pwNodeX['In'])
    fc.connectTerminals(bufferNodeY['dataOut'], pwNodeY['In'])
    fc.connectTerminals(bufferNodeZ['dataOut'], pwNodeZ['In'])

    #fc.connectTerminals(bufferNode['dataOut'], pw1Node['In'])
    win.show()
    app.exec_()