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
    # 3중 for문에서 찾은 노드와 엣지를 저장하기 위한 리스트
    nodes = []
    src_nodes = []
    dst_nodes = []
    edges = []

    # graph에서 불러온 격자의 크기
    xDim = ctypes.c_int()
    yDim = ctypes.c_int()
    zDim = ctypes.c_int()
    graph.getDim(xDim, yDim, zDim)
    xDim = xDim.value
    yDim = yDim.value
    zDim = zDim.value

    # 3중 for문에서 찾은 노드를 임시적으로 저장하기 위한 변수
    v = frPoint()
    w = frPoint()

    # 모든 그래프를 순차적으로 탐색하며 노드를 저장
    for xIdx in range(xDim):
        for yIdx in range(yDim):
            for zIdx in range(zDim):
                v = graph.getPoint(v, xIdx, yIdx)
                node = (v.x(), v.y(), zIdx)
                nodes.append(node)
                if graph.isSrc(xIdx, yIdx, zIdx): # Source 노드 저장
                    src_nodes.append(node)
                if graph.isDst(xIdx, yIdx, zIdx): # Destination 노드 저장
                    dst_nodes.append(node)
                if graph.hasEdge(xIdx, yIdx, zIdx, frDirEnum.N): # x축 방향으로 존재햐는 엣지의 양 노드 저장
                    w = graph.getPoint(w, xIdx, yIdx+1)
                    edges.append((node, (w.x(), w.y(), zIdx)))
                if graph.hasEdge(xIdx, yIdx, zIdx, frDirEnum.E): # y축 방향으로 존재하는 엣지의 양 노드 저장
                    w = graph.getPoint(w, xIdx+1, yIdx)
                    edges.append((node, (w.x(), w.y(), zIdx)))
                if graph.hasEdge(xIdx, yIdx, zIdx, frDirEnum.U): # z축 방향으로 존재하는 엣지의 양 노드 저장
                    edges.append((node, (v.x(), v.y(), zIdx+1)))

    # 3D 그래프를 그릴 공간
    ax = plt.figure().add_subplot(111, projection='3d')
    
    # 엣지를 파란색 실선으로 표현
    for (ex1, ey1, ez1), (ex2, ey2, ez2) in edges:
        ax.plot([ex1, ex2], [ey1, ey2], [ez1, ez2], 'b-', linewidth=0.3)

    # 모든 노드를 회색 점으로 표현
    if nodes:
        ax.scatter(*zip(*nodes), c='gray', s=3)

    # Source 노드를 초록색 점으로 표현
    if src_nodes:
        ax.scatter(*zip(*src_nodes), c='green', s=30, label='Source')

    # Destination 노드를 빨간색 점으로 표현
    if dst_nodes:
        ax.scatter(*zip(*dst_nodes), c='red', s=30, label='Destination')

    # 경로를 노란색 실선으로 표현
    if path:
        px, py, pz = zip(*path)
        ax.plot(px, py, pz, 'y-', linewidth=3, label='Path')
        ax.scatter(px, py, pz, c='yellow', s=30)

    # 라벨 표시, 그래프 제목 지정, 그래프 시각화
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
