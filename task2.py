graph={
    'a':{'b':2,'d':4},
    'b':{'a':2,'c':3},
    'c':{'b':3,'d':1},
    'd':{'c':1,'a':4}
    }
print("Edges and their cost");
seen=set ()
for node,edges in graph.items():
    for neighbor,cost in edges.items():
        if (neighbor,node) not in seen:
            print(f"{node} -> {neighbor} : cost = {cost}")
            seen.add((node,neighbor))
cycle_path=['a','b','c','d','a']
total_cost=0
for i in range(len(cycle_path)-1):
    start=cycle_path[i]
    end=cycle_path[i+1]
    cost=graph[start][end]
    total_cost+=cost
print(f"\nTotal cost of the cycle {cycle_path} is : {total_cost}")
cycle_path=['a','b','c','d']
total_cost=0
for i in range(len(cycle_path)-1):
    start=cycle_path[i]
    end=cycle_path[i+1]
    cost=graph[start][end]
    total_cost+=cost
print(f"\nTotal cost of the cycle {cycle_path} is : {total_cost}")
