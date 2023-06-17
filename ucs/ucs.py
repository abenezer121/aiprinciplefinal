from pq import CustomProrityQueue
class UniformCostSearch:
    def ucs(self,start, goal, state_graph):
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
    
    def ucscustom(self,start, goal_array, state_graph):
        frontier = CustomProrityQueue(start)
        visited = set()
        prev = {start:None}
        path = [] 
        total_cost = 0 
    
        while frontier.q and goal_array:
            cost, curr = frontier.pop()
            if curr in goal_array: 
                goal_array.remove(curr) 
                p = []
                while curr is not None:
                        p.append(curr)
                        curr = prev[curr]
                p.reverse()

                total_cost += cost 
                path.extend(p[1:]) 
                start = p[-1] 
                frontier = CustomProrityQueue(start) 
                visited = set()
                prev = {start:None} 
        
            else: 
                visited.add(curr)
        
                for adj in state_graph[curr]:
                    if adj not in visited:
                        if adj not in frontier.states:
                            prev[adj]=curr
                            frontier.add(adj,cost+state_graph[curr][adj])
                        elif frontier.states[adj] > cost+state_graph[curr][adj]:
                            prev[adj]=curr
                            frontier.replace(adj,cost+state_graph[curr][adj])
        
        return path, total_cost 



   