
import numpy as np
from pq import CustomizedPriorityQueue


class Astar:


    def astar_search(self,start, goal, state_graph):
        queue = CustomizedPriorityQueue(start)
        visited = set()
        prev = {start:None}
    
        while queue.priority_queue:
            cost, curr = queue.pop()
            visited.add(curr)
            if curr == goal:
                #get the path
                p = []
                while curr is not None:
                    p.append(curr)
                    curr = prev[curr]
                p.reverse()
                #get the cost
                total = 0 
                for i in range(len(p)-1): 
                    total += state_graph[p[i]][p[i+1]]
                
              
                return p, total
            
            for adj in state_graph[curr]:
                if adj not in visited:
                    new_cost = cost + state_graph[curr][adj] 
                    if adj not in queue.state_cost_map:
                        prev[adj] = curr
                        queue.add(adj, new_cost)
                    elif queue.state_cost_map[adj] > new_cost:
                        prev[adj] = curr
                        queue.replace(adj, new_cost)




