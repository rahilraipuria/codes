import heapq

class Graph:
    
    def __init__(self,adjMatrix):
        self.graph = adjMatrix
        self.n = len(adjMatrix)
        
    def uniformCostSearch(self,start,goal):
        
        pq = []
        heapq.heappush(pq,(0,start,[start]))
        visited = {}
        
        while pq:
            
            currentCost, node, path = heapq.heappop(pq)
            
            if node in visited and visited[node]<=currentCost:
                continue
            
            visited[node] = currentCost
            
            if node == goal:
                print(f"Path to goal {goal} with total cost {currentCost} : {'->'.join(map(str,path))}")
                return path
            
            
            for neighbor in range(self.n):
                if self.graph[node][neighbor] > 0:
                    newCost = currentCost + self.graph[node][neighbor]
                    heapq.heappush(pq,(newCost,neighbor,path + [neighbor]))
                    
        print("Goal cannot be reached")
        return None
        
    
def main():
    numNodes = int(input("Enter no. of Nodes: "))
    print("Enter Adjacency Matrix : ")
    
    adjMatrix = [list(map(int, input().split())) for _ in range(numNodes)]
    
    g = Graph(adjMatrix)
    
    startNode = int(input("Enter Start Point: "))
    goalNode = int(input("Enter Goal: "))
    
    g.uniformCostSearch(startNode,goalNode)
    
    
if __name__ == "__main__":
    main()