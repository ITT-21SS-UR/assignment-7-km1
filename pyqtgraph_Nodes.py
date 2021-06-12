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
    Creates Normal Vector
    """
    nodeName = "NormalVector"

    def __init__(self, name):
        terminals = {
            'normalX': dict(io='in'),
            'normalZ': dict(io='in'),
            'outVector': dict(io='out')
        }

        Node.__init__(self, name, terminals=terminals)

    def process(self, **kwds):
        return [(0, 0), (1.0, 1.0)]


fclib.registerNodeType(NormalVectorNode, [('Data', )])