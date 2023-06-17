class Problem: 
    def __init__(self, initial, goal=None):
       self.initial = initial
       self.goal = goal

    def goal_test(self, state):
        return state == self.goal
    
    def actions(self, state):
         raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError
            
    def value(self, state):
        raise NotImplementedError
  
   
class GraphProblem(Problem):  
    def __init__(self, initial, goal, graph):
        Problem.__init__(self, initial, goal)
        self.graph = graph
    def actions(self, A):        
        return self.graph.get(A)
    def result(self, state, action):
        return action