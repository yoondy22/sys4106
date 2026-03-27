import argparse
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from game import *

def printGraph(graph):
    gridBBox = frBox()

    graph.getBBox(gridBBox)

    print(f"printing Maze grid ({gridBBox.left()},{gridBBox.bottom()}) ... ({gridBBox.right(),gridBBox.top()})")

    xDim = ctypes.c_int()
    yDim = ctypes.c_int()
    zDim = ctypes.c_int()
    graph.getDim(xDim, yDim, zDim)
    xDim = xDim.value
    yDim = yDim.value
    zDim = zDim.value

    print(f"extBBox (xDim, yDim, zDim) = ({xDim},{yDim},{zDim})")

    v = frPoint()
    w = frPoint()

    for xIdx in range(xDim):
        for yIdx in range(yDim):
            for zIdx in range(zDim):
                if graph.isSrc(xIdx, yIdx, zIdx):
                    print(f"({xIdx}, {yIdx}, {zIdx}) is a source node.")
                if graph.isDst(xIdx, yIdx, zIdx):
                    print(f"({xIdx}, {yIdx}, {zIdx}) is a destination node.")
                if (graph.hasEdge(xIdx, yIdx, zIdx, frDirEnum.N)):
                    v = graph.getPoint(v, xIdx, yIdx)
                    w = graph.getPoint(w, xIdx, yIdx+1)
                    print(f"The x,y coordinates of node ({xIdx}, {yIdx}, {zIdx}) is ({v.x()}, {v.y()}).")
                    print(f"The x,y coordinates of node ({xIdx}, {yIdx+1}, {zIdx}) is ({w.x()}, {w.y()}).")
                if (graph.hasEdge(xIdx, yIdx, zIdx, frDirEnum.E)):
                    v = graph.getPoint(v, xIdx, yIdx)
                    w = graph.getPoint(w, xIdx+1, yIdx)
                    print(f"The x,y coordinates of node ({xIdx}, {yIdx}, {zIdx}) is ({v.x()}, {v.y()}).")
                    print(f"The x,y coordinates of node ({xIdx+1}, {yIdx}, {zIdx}) is ({w.x()}, {w.y()}).")
                if (graph.hasEdge(xIdx, yIdx, zIdx, frDirEnum.U)):
                    v = graph.getPoint(v, xIdx, yIdx)
                    print(f"The x,y coordinates of node ({xIdx}, {yIdx}, {zIdx}) is ({v.x()}, {v.y()}).")
                    print(f"The x,y coordinates of node ({xIdx}, {yIdx}, {zIdx+1}) is ({v.x()}, {v.y()}).")

def plotMyGridGraph(graph, path=None):
    nodes = []
    src_nodes = []
    dst_nodes = []
    edges = []

    xDim = ctypes.c_int()
    yDim = ctypes.c_int()
    zDim = ctypes.c_int()
    graph.getDim(xDim, yDim, zDim)
    xDim = xDim.value
    yDim = yDim.value
    zDim = zDim.value

    v = frPoint()
    w = frPoint()

    for xIdx in range(xDim):
        for yIdx in range(yDim):
            for zIdx in range(zDim):
                v = graph.getPoint(v, xIdx, yIdx)
                node = (v.x(), v.y(), zIdx)
                nodes.append(node)
                if graph.isSrc(xIdx, yIdx, zIdx):
                    src_nodes.append(node)
                if graph.isDst(xIdx, yIdx, zIdx):
                    dst_nodes.append(node)
                if graph.hasEdge(xIdx, yIdx, zIdx, frDirEnum.N):
                    w = graph.getPoint(w, xIdx, yIdx+1)
                    edges.append((node, (w.x(), w.y(), zIdx)))
                if graph.hasEdge(xIdx, yIdx, zIdx, frDirEnum.E):
                    w = graph.getPoint(w, xIdx+1, yIdx)
                    edges.append((node, (w.x(), w.y(), zIdx)))
                if graph.hasEdge(xIdx, yIdx, zIdx, frDirEnum.U):
                    edges.append((node, (v.x(), v.y(), zIdx+1)))

    ax = plt.figure().add_subplot(111, projection='3d')
    
    for (ex1, ey1, ez1), (ex2, ey2, ez2) in edges:
        ax.plot([ex1, ex2], [ey1, ey2], [ez1, ez2], 'b-', linewidth=0.3)

    if nodes:
        ax.scatter(*zip(*nodes), c='gray', s=3)

    if src_nodes:
        ax.scatter(*zip(*src_nodes), c='green', s=30, label='Source')

    if dst_nodes:
        ax.scatter(*zip(*dst_nodes), c='red', s=30, label='Destination')

    if path:
        px, py, pz = zip(*path)
        ax.plot(px, py, pz, 'y-', linewidth=3, label='Path')
        ax.scatter(px, py, pz, c='yellow', s=30)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z (Layer)')
    ax.legend()
    plt.title('3D Grid Graph')
    plt.savefig('grid_graph.png')
    plt.show()

    try:
        printGraph(graph)
    except Exception as e:
        traceback.print_exec()
        os.exit_(1)