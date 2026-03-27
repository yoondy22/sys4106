# SYS4106 Lab 1 Report
**2022189103 윤도영**  
**2025.03.27**

---

## Overview

The goal of this lab is to modify `plotGraph.py` to visualize the 3D grid graph used in TritonRoute.

---

## Idea

1. Use ChatGPT to summarize and understand the `sys4106` repo efficiently.
   (For the given `plotGraph.py` code, ask ChatGPT to explain it line-by-line to understand in detail.)
2. Get hints from `printGraph` to write `plotMyGridGraph`.
3. When drawing the graph in `plotMyGridGraph`, split the code into two parts for better readability — one part for 'finding nodes', and another for 'drawing the graph'.
4. Detailed explanations of the code are written as comments inside `plotGraph.py`.

---

## Implementation

1. Make lists to store the found nodes.
2. Write the node-finding code in a similar way to the `printGraph` function.
   (The key difference from `printGraph` is that `plotMyGridGraph` stores the nodes, while `printGraph` prints them.)
3. Plot all nodes as gray dots, source nodes as green dots, destination nodes as red dots, edges as blue lines, and the path as a yellow line.
4. After ChatGPT generated the initial code, the graph design — such as node size and line colors — was fine-tuned by making small adjustments.

---

## ChatGPT Prompts Used

1. lab_1.pdf, github.com/jaeyongchung/sys4106 를 읽고, 조건에 맞도록 plotGraph.py에서 Your Code Here 부분을 작성해줘.
2. 이제 이 코드와 과정 전체를 처음부터 이해하고 공부하고 싶은데 설명해줄 수 있어?
3. 일단 이 과제를 리눅스로 진행해야 하는 이유가 뭐야?
4. EDA가 뭐야?
5. cppyy 라는게 뭐야?
6. 이제 openroad와 tritonroute에 대해 설명해줘.
7. 근데 과제 안내서에 openraod를 써야 하지만, 이 과제에서는 openroad 대신에 OpenFASOC를 설치해서 사용하게 된다고 하잖아. 왜 그런 거야?
8. 이제 lab_1.pdf의 python binding 부분을 설명해줘.
9. 너가 이 코드를 작성할 때, def plotMyGridGraph(graph):부분을 def plotMyGridGraph(graph, path=None):로 수정했잖아. 근데 주어진 코드들은 plotMyGridGraph 함수를 호출할 때 지금은 path를 넘겨주지 않을텐데, 이건 나중에 path가 제공될 때를 대비한 수정인 거야?
10. routeNet() 함수 안에서 A* 탐색 직전에 plot한다는 건 무슨 뜻이야? 탐색을 모두 마친 뒤에 그래프을 그리는 거인 줄 알았는데, 탐색하기 전에 노드들의 위치부터 그래프로 나타내보는 거야?
11. 그럼 route.py의 구조부터 간단히 파악해보고 싶어. route.py의 함수들에 대해 간단히 설명해줘.
12. 아래처럼 두 줄로 작성된 코드를 한 줄로 작성해도 되지? `fig`라는 변수는 어차피 이 부분 말고 안 쓰이잖아.
```python
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
```
```python
    ax = plt.figure().add_subplot(111, projection='3d')
```
13. 가시성을 해치지 않고, 성능을 크게 저하시키지 않는 선에서 아래 코드를 최대한 간소화하고 싶은데, 이것도 좀 더 간소화할 수 있어?
```python
    for edge in edges:
        x = [edge[0][0], edge[1][0]]
        y = [edge[0][1], edge[1][1]]
        z = [edge[0][2], edge[1][2]]
        ax.plot(x, y, z, 'b-', linewidth=0.5)
```
14. 그럼 `nx, ny, nz = zip(*nodes)` 부분도 `ax.scatter`에 바로 집어넣을 수 있겠네?

---

## Results

All nodes and edges are plotted on the graph correctly.
All four requirements given in the problem are also satisfied.

1. **Source nodes** are marked in **green** and **destination nodes** in **red**. Multiple sources and destinations are correctly displayed.
2. `path` was added as a parameter to `plotMyGridGraph`, and it will be highlighted in **yellow** if provided.
3. The graph is plotted in **3D**.
4. `matplotlib` is used for visualization.
