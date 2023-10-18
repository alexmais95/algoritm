graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

infinity = float('inf')
coasts = {}
coasts['a'] = 6
coasts['b'] = 2
coasts['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None


def find_lovest(costs):
    lovest = float('inf')
    lovest_node = None
    for node in costs:
        cost = costs[node]
        if cost < lovest and node not in procesed:
            lovest = cost
            lovest_node = node
    return lovest_node


procesed = []
node = find_lovest(coasts)
while node is not None:
    cost = coasts[node]
    neighborns = graph[node]
    for n in neighborns.keys():
        new_cost = cost + neighborns[n]
        if coasts[n] > new_cost:
            coasts[n] = new_cost
            parents[n] = node
    procesed.append(node)
    node = find_lovest(coasts)