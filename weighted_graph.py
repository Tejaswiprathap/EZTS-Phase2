graph={}
def add_node(v):
    if v in graph:
        print("Node is already present in graph")
    else:
        graph[v]=[]
def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1," is not present")
    if v2 not in graph:
        print(v2," is not present")
    else:
        list1=[v2,cost]
        list2=[v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)
def delete_node(v):
    if v not in graph:
        print(f"node {v} is not present")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in graph[i]:
                list1.remove(v)
'''def delete_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1," is not present")
    if v2 not in graph:
        print(v2," is not present")
    else:
        list1=[v2,cost]
        list2=[v1,cost]
        if v1 in graph[v2]:
            graph[v2].remove(list1)
        if v2 in graph[v1]:
            graph[v1].remove(list2)'''
print(graph)
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A","B",5)
add_edge("A","E",4)
add_edge("A","D",2)
add_edge("D","C",4)
delete_node("B")
#delete_edge("A","B",5)
print(graph)
