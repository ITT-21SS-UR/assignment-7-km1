"""
Code written by Kay Brinkmann and reviewed by Marco Beetz
Overall structure based on DIPPID_pyqtnode.py
"""

import sys
from pyqtgraph.flowchart import Flowchart, Node
from pyqtgraph.flowchart.library.common import CtrlNode
import pyqtgraph.flowchart.library as fclib
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
from DIPPID_pyqtnode import BufferNode, DIPPIDNode
from pyqtgraph_Nodes import LogNode, NormalVectorNode


if __name__ == '__main__':
    # close app if none or too many arguments were given
    if len(sys.argv) == 2:
        port = sys.argv[1]
    else:
        print("You need to specify the port you want to connect to. Do not add any other arguments")
        sys.exit()
    app = QtGui.QApplication([])
    win = QtGui.QMainWindow()

    # sets up layout
    win.setWindowTitle('Analyze DIPPID Data')
    cw = QtGui.QWidget()
    win.setCentralWidget(cw)
    layout = QtGui.QGridLayout()
    cw.setLayout(layout)
    fc = Flowchart(terminals={})
    w = fc.widget()
    layout.addWidget(fc.widget(), 0, 0, 2, 1)
    pwX = pg.PlotWidget()
    pwY = pg.PlotWidget()
    pwZ = pg.PlotWidget()
    pwNormal = pg.PlotWidget()
    layout.addWidget(pwX, 0, 1)
    layout.addWidget(pwY, 0, 2)
    layout.addWidget(pwZ, 1, 1)
    layout.addWidget(pwNormal, 1, 2)
    pwX.setYRange(0, 4)
    pwX.setTitle("Accelerometer X")
    pwY.setYRange(0, 4)
    pwY.setTitle("Accelerometer Y")
    pwZ.setYRange(0, 4)
    pwZ.setTitle("Accelerometer Z")
    pwNormal.setYRange(-5, 5)
    pwNormal.setXRange(-5, 5)
    pwNormal.setTitle("Normal Vector")

    # sets up flowchart nodes
    dippidNode = fc.createNode("DIPPID", pos=(0, 0))
    # sets up specified port number and connects to device
    dippidNode.text.setText(port)
    dippidNode.connect_device()
    bufferNodeX = fc.createNode("Buffer", pos=(150, -100))
    pwNodeX = fc.createNode('PlotWidget', pos=(300, -100))
    pwNodeX.setPlot(pwX)
    bufferNodeY = fc.createNode("Buffer", pos=(150, 0))
    pwNodeY = fc.createNode('PlotWidget', pos=(300, 0))
    pwNodeY.setPlot(pwY)
    bufferNodeZ = fc.createNode("Buffer", pos=(150, 100))
    pwNodeZ = fc.createNode('PlotWidget', pos=(300, 100))
    pwNodeZ.setPlot(pwZ)
    pwNodeNormal = fc.createNode('PlotWidget', pos=(300, 100))
    pwNodeNormal.setPlot(pwNormal)
    normalVectorNode = fc.createNode("NormalVector", pos=(150, 100))
    logNode = fc.createNode("Log", pos=(450, 0))

    # sets up node connections for the vuffer nodes an plots
    fc.connectTerminals(dippidNode['accelX'], bufferNodeX['dataIn'])
    fc.connectTerminals(dippidNode['accelY'], bufferNodeY['dataIn'])
    fc.connectTerminals(dippidNode['accelZ'], bufferNodeZ['dataIn'])
    fc.connectTerminals(bufferNodeX['dataOut'], pwNodeX['In'])
    fc.connectTerminals(bufferNodeY['dataOut'], pwNodeY['In'])
    fc.connectTerminals(bufferNodeZ['dataOut'], pwNodeZ['In'])

    # sets up node connection for normal vector and log nodes change input nodes for different normal vectors or logs
    fc.connectTerminals(dippidNode['accelZ'], normalVectorNode['inputAccel1'])
    fc.connectTerminals(dippidNode['accelX'], normalVectorNode['inputAccel2'])
    fc.connectTerminals(normalVectorNode['outVector'], pwNodeNormal['In'])
    fc.connectTerminals(normalVectorNode['outVector'], logNode['dataIn'])

    win.show()
    sys.exit(app.exec_())
