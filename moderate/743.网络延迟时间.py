import heapq#堆列heap queue
from typing import List
"""有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 
times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， 
wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。"""
#我是完全无法理解这个算法
#dijkstra算法，图论算法中最短路之一
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #这里似乎是在做数据处理
        graph = [[] for _ in range(n)]
        for u,v,w in times:
            graph[u-1].append((v-1,w))
        dist = [float('inf')]*n
        dist[k-1] = 0
        #这里是这个算法的精髓，优先对列
        pq = [(0,k-1)]

        while pq:
            #我就先找哪个最短，完全不管这个路是去哪里的
            d,u = heapq.heappop(pq)
            #这里优化了一下
            if d>dist[u]:
                continue
            for v,w in graph[u]:
                nd = d+w#这里也是邻居的意思
                if nd<dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq,(nd,v))
        ans = max(dist)
        return -1 if ans==float('inf') else int(ans)