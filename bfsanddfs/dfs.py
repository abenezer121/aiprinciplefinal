from node import Node
class dfs:
    def depth_first_search(problem):
    
        frontier = [(Node(problem.initial))]

        explored = set()
        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                return node
            explored.add(node.state)
            frontier.extend(child for child in node.expand(problem)
                            if child.state not in explored and child not in frontier)
        return None