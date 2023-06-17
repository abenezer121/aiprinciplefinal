
import numpy as np
from pq import CustomizedPriorityQueue
from pqucs import CustomProrityQueue

class Astar:

    def heuristic(self , start , goal , state_graph):
        frontier = CustomProrityQueue(start)
        visited = set()
        prev = {start:None}
    
        while frontier.q:
            cost, curr = frontier.pop()
            if curr == goal:
                # p = path(prev, curr)
                p = []
                while curr is not None:
                        p.append(curr)
                        curr = prev[curr]
                p.reverse()

                total = 0 
                for i in range(len(p)-1): 
                        total += state_graph[p[i]][p[i+1]]
                return p, total 
            visited.add(curr)
        
            for adj in state_graph[curr]:
                if adj not in visited:
                    if adj not in frontier.states:
                        prev[adj]=curr
                        frontier.add(adj,cost+state_graph[curr][adj])
                    elif frontier.states[adj] > cost+state_graph[curr][adj]:
                        prev[adj]=curr
                        frontier.replace(adj,cost+state_graph[curr][adj])
    


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
                    path,h = self.heuristic(adj , goal ,state_graph )
                    new_cost = cost + state_graph[curr][adj]+h 
                    if adj not in queue.state_cost_map:
                        prev[adj] = curr
                        queue.add(adj, new_cost)
                    elif queue.state_cost_map[adj] > new_cost:
                        prev[adj] = curr
                        queue.replace(adj, new_cost)




