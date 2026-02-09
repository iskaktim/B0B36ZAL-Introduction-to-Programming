class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.edges = []
        self.minDistance = float('inf')
        self.previousVertex = None


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Dijkstra:
    def __init__(self):
        self.vertexes = []


    def getVertexWithSmallestMinDistance(self, pq):
        min_value_index = 0
        for i in range(len(pq)):
            if pq[i].minDistance < pq[min_value_index].minDistance:
                min_value_index = i
        return pq.pop(min_value_index)

    def computePath(self, sourceId):
        visited_vertexes = []
        priority_queue = []
        start_vertex = self.getVertexById(sourceId)
        start_vertex.minDistance = 0
        priority_queue.append(start_vertex)
        while priority_queue != []:
            act_vertex = self.getVertexWithSmallestMinDistance(priority_queue)
            visited_vertexes.append(act_vertex)
            for edge in act_vertex.edges:
                neighboar_vertex = self.getVertexById(edge.target)
                if neighboar_vertex not in visited_vertexes:
                    if neighboar_vertex not in priority_queue:
                        priority_queue.append(neighboar_vertex)
                    if act_vertex.minDistance + edge.weight < neighboar_vertex.minDistance:
                        neighboar_vertex.minDistance = act_vertex.minDistance + edge.weight
                        neighboar_vertex.previousVertex = act_vertex

        
    def getVertexById(self, search_id:int)->Vertex|None:
        for vertex in self.vertexes:
            if vertex.id == search_id:
                return vertex
        return None
    
    def getShortestPathTo(self, targetId):
        result = []
        act_vertex = self.getVertexById(targetId)

        while act_vertex is not None:
            result.insert(0, act_vertex)
            act_vertex = act_vertex.previousVertex

        return result


    def createGraph(self, vertexes, edgesToVertexes):
        self.vertexes = vertexes
        for vertex in vertexes:
            for edge in edgesToVertexes:
                if vertex.id == edge.source:
                    vertex.edges.append(edge)

    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = float('inf')
            vertex.previousVertex = None

    def getVertexes(self):
        return self.vertexes
