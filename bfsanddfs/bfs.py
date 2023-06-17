from node import Node
from collections import deque

class bfs:
    #breadth first search strategy
    def breadth_first_search(problem): 
        node = Node(problem.initial)
        if problem.goal_test(node.state):
            return node
        frontier = deque([node])
        explored = set()
        while frontier:
            node = frontier.popleft()
            explored.add(node.state)
            for child in node.expand(problem):
                if child.state not in explored and child not in frontier:
                    if problem.goal_test(child.state):
                        return child
                    frontier.append(child)
        return None