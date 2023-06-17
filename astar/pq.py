# import heapq
# class CustomizedPriorityQueue():
#     def __init__(self, start, cost = 0):
#         self.start = start
#         self.cost = cost
#         self.states = {start:cost} 
#         self.q = [[cost, start]]
    
#     def add(self,state,cost):
#         self.states[state]=cost
#         heapq.heappush(self.q,[cost,state])
    
#     def pop(self):
#         return heapq.heappop(self.q)
    
#     def replace(self,state,cost):
#         self.states[state]=cost
#         for i,tup in enumerate(self.q):
#             if tup[1]==state:
#                 self.q[i][0]=cost

import heapq
class CustomizedPriorityQueue():
    def __init__(self, initial_state, initial_cost = 0):
        self.initial_state = initial_state
        self.initial_cost = initial_cost
        self.state_cost_map = {initial_state:initial_cost} 
        self.priority_queue = [[initial_cost, initial_state]]
    
    def add(self,new_state,new_cost):
        self.state_cost_map[new_state]=new_cost
        heapq.heappush(self.priority_queue,[new_cost,new_state])
    
    def pop(self):
        return heapq.heappop(self.priority_queue)
    
    def replace(self,old_state,new_cost):
        self.state_cost_map[old_state]=new_cost
        for i,pair in enumerate(self.priority_queue):
            if pair[1]==old_state:
                self.priority_queue[i][0]=new_cost
