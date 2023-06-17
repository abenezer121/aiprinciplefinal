
class DepthFirstSearch:
    
    def dfs(map, initial, goal):
      stack = []
      stack.append(initial)
  
      parent = {}
      parent[initial] = None
      while stack:
        node = stack.pop()
        if node == goal:
          break
        for neighbor in map[node]:
          if neighbor not in parent:
            stack.append(neighbor)
            parent[neighbor] = node
      path = []
      if goal in parent:
        current = goal
        while current != initial:
          path.append(current)
          current = parent[current]
        path.append(initial)
        path.reverse()
      return path
