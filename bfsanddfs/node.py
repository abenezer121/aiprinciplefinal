class Node: 
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action 
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
    def __repr__(self): 
        return "<Node "+ self.state + ">"
    def expand(self, problem): 
        children = []
        for action in problem.actions(self.state):
            x=self.child_node(problem,action)
            children.append(x)
        return children
    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action )   
        return next_node   
    def path(self): 
        node, path_back = self, []
        while node: 
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back)) 
    def solution(self): 
        return [node.state for node in self.path()]