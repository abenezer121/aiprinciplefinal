from astar import Astar
from mapclass import mapclass
print("running a star")

astar = Astar()
path , cost = astar.astar_search("Addis Ababa", "Moyale", mapclass.return_map())
print("path using a star is  ", path , " with cost of ",cost)