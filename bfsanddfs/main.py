
  
from graph import Graph
from data import Data
from node import Node   
from problem import GraphProblem
from dfs import dfs
from bfs import bfs

visit_ethiopia= Graph(Data.returnmap(),False)




visit_ethiopia_problem = GraphProblem('Addis Ababa','Shire', visit_ethiopia)
finalnode = bfs.breadth_first_search(visit_ethiopia_problem)
print("breadth_first_search of ", visit_ethiopia_problem.initial, " to ", visit_ethiopia_problem.goal, finalnode.solution())



finalnode = dfs.depth_first_search(visit_ethiopia_problem)
 
print("depth_first_search of ", visit_ethiopia_problem.initial, " to ", visit_ethiopia_problem.goal, finalnode.solution())
