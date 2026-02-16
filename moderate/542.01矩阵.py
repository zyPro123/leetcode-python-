from collections import deque   # 1. 导入高效队列
from typing import List
"""给定一个由 0 和 1 组成的矩阵 mat ，
请输出一个大小相同的矩阵，
其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。

两个相邻元素间的距离为 1 """
#图论算法，BFS,广度优先算法，和dp不是一个东西
#个人理解偏向液体扩散
def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    dist = [[-1] * n for _ in range(m)]
    queue = deque()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                #通过先进先出的方式来放置我这一次主动扩散的点
                queue.append((i, j))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            n_x, n_y = x + dx, y + dy
            if 0 <= n_x < m and 0 <= n_y < n and dist[n_x][n_y] == -1:
                #这里n是neibourhood,如果邻居已经扩散一遍了，就不要再来一次了
                dist[n_x][n_y] = dist[x][y] + 1
                queue.append((n_x, n_y))
    return dist