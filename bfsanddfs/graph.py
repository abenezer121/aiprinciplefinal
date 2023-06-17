class Graph: 
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed        
    def nodes(self):        
        return list(self.graph_dict.keys())    
    def get(self, a, b=None):
        links = self.graph_dict.get(a) 
        if b is None:
            return links    