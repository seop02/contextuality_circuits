from layers import *
import numpy as np

dev = qml.device('default.qubit', wires = 8)
@qml.qnode(dev)
def QCNN_1(U, params):
    layer1(U, params)
    return qml.state()
    
dev = qml.device('default.qubit', wires = 8)
@qml.qnode(dev)
def QCNN_2(U, params1, params2):
    layer1(U, params1)
    layer2(U, params2)
    return qml.state()
    
dev = qml.device('default.qubit', wires = 8)
@qml.qnode(dev)
def QCNN_3(U, params1, params2, params3):
    layer1(U, params1)
    layer2(U, params2)
    layer3(U, params3)
    return qml.state()