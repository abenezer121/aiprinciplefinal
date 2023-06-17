
  

from data import Data
from bfs import BreadthFirstSearch
from dfs import DepthFirstSearch

map =  Data.returnmap()


print("using breadth first search")
# Call the function with an initial and a goal state
print(BreadthFirstSearch.breadth_first_search(map, "Addis Ababa", "Awash"))
print()
print()

print("using depth first search")
print(DepthFirstSearch.dfs(map, "Addis Ababa", "Jimma"))








