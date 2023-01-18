from collections import defaultdict

def criticalpaths(n,paths):
    if not paths: return None
    graph =defaultdict(list)
    distances={}
    visited=set[(0)]
    critical_paths=list()

    def dfs(node,parent,distance):
        cur_distance=distance
        distances[node]=distance
        lowest_reach=distance

        for neighbor in graph[node]:
            if neighbornot in visited:
                visited.add(neighbor)
                lowest,distance=dfs(neighbor,node,distance)
                if lowest>cur_distance:
                    critical_paths.append((node,neighbor))
            
                lowest_reach=min(lowest_reach,lowest)
            elif neighbor!=parent:
                lowest_reach=min(lowest_reach,distances[neighbor])


        return(lowest_reach,distance)

    for u,v in paths:
        graph[u].append(v)
        graph[v].append(u)
    
    dfs(0,None,1)
    return critical_paths

    res=[]
    graph=make_graph(paths)
    visited={}
    dfs(0,0,float('inf'))
    return res
            
path,planet=map(int,input().split())
paths=[]
for i in range(path):
    temp=list(map(input().split()))
    paths.append(temp)

bridges=criticalpaths(planet,paths)
cp=[]
for i in bridges():
    cp.append(i[0])
    cp.append(i[1])

ans=list(set(cp))
ans.sort()
if(len(ans)==0):
    print(-1)

