from pyqtgraph.flowchart import Flowchart, Node
from pyqtgraph.flowchart.library.common import CtrlNode
import pyqtgraph.flowchart.library as fclib
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
from DIPPID import SensorUDP, SensorSerial, SensorWiimote
import sys


class LogNode(Node):
    """
    Logs nodes input to stdout
    """
    nodeName = "Log"

    def __init__(self, name):
        terminals = {
            'dataIn': dict(io='in'),
        }
        Node.__init__(self, name, terminals=terminals)

    def process(self, **kwds):
        print(kwds["dataIn"])
        return


fclib.registerNodeType(LogNode, [('Logging', )])


class NormalVectorNode(Node):
    """
    Creates Normal Vector for two input accels.
    Overall Structure based on the buffer node from DIPPID_pyqtnode.py
    """
    nodeName = "NormalVector"

    def __init__(self, name):
        terminals = {
            'inputAccel1': dict(io='in'),
            'inputAccel2': dict(io='in'),
            'outVector': dict(io='out')
        }
        Node.__init__(self, name, terminals=terminals)

    def process(self, **kwds):
        print("processed")
        self._vector = np.array([[0, 0], [kwds['inputAccel1'][0], kwds['inputAccel2'][0]]])
        print("processed2")
        print("Vector:", self._vector)
        return {'outVector': self._vector}


fclib.registerNodeType(NormalVectorNode, [('Data', )])
