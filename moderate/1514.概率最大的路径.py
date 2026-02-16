import heapq
from typing import List
"""给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，
其中 edges[i] = [a, b] 表示连接节点 a 和 b 的一条无向边，且该边遍历成功的概率为 succProb[i] 。
指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。
如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。"""\
#dijkstra,依然是动态规划+贪心算法，只不过这里是权重相乘得最大值
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        #把数据转换成方便使用的样子
        graph = [[]*n for _ in range(n)]
        for i,(u,v) in enumerate(edges):
            p = succProb[i]
            #无向其实就是双向，u回事v，v就是u
            graph[u].append((v,p))
            graph[v].append((u,p))

        prob = [0.0]*n
        prob[start_node] = 1.0
        #用负数是因为heapq返回的是最小值
        '''这里就是贪心算法的体现，我利用之前的信息，从这里面弹出的就是最值'''
        """由于满足单调性，如果你一条路就比我全部大了，那都不配进入比较"""
        pq = [(-1.0,start_node)]
        while pq:
            neg_p,u = heapq.heappop(pq)
            cur_p = -neg_p
            #两个if优化算法，一些确定的情况直接跳过
            if cur_p<prob[u]:#比完后会还剩残余的，直接过
                continue
            if u==end_node:#最后一个肯定是最值
                return cur_p
            '''这里不是在求u的最值，是v的'''
            for v,w in graph[u]:
                new_p = cur_p*w
                if new_p>prob[v]:
                    prob[v] = new_p
                    heapq.heappush(pq,(-new_p,v))
        return prob[end_node]