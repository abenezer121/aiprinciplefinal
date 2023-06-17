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
        path = [] # initialize an empty list to store the final path
        total_cost = 0 # initialize a variable to store the total cost
    
        while frontier.q and goal_array: # loop until the frontier is empty or all goals are reached
            cost, curr = frontier.pop()
            if curr in goal_array: # check if the current city is in the goal array
                goal_array.remove(curr) # remove it from the goal array
                # p = path(prev, curr)
                p = []
                while curr is not None:
                        p.append(curr)
                        curr = prev[curr]
                p.reverse()

                total_cost += cost # update the total cost with the cost to reach the current goal city
                path.extend(p[1:]) # extend the final path with the partial path to the current goal city (excluding the start city)
                start = p[-1] # update the start city to be the current goal city
                frontier = CustomProrityQueue(start) # reinitialize the frontier with the new start city
                visited = set() # reset the visited set
                prev = {start:None} # reset the prev dictionary
        
            else: # if the current city is not a goal city, continue the search as usual
                visited.add(curr)
        
                for adj in state_graph[curr]:
                    if adj not in visited:
                        if adj not in frontier.states:
                            prev[adj]=curr
                            frontier.add(adj,cost+state_graph[curr][adj])
                        elif frontier.states[adj] > cost+state_graph[curr][adj]:
                            prev[adj]=curr
                            frontier.replace(adj,cost+state_graph[curr][adj])
        
        return path, total_cost # return the final path and cost to reach all the goal cities



   