
graph = {}

def build_graph(listofCurrency):

    def add_edge(first, second, value):
        if first in graph:
            graph[first].append((second, value))
        else:
            graph[first] = [(second, value)]

    listofCurrency = list(listofCurrency.split(";"))
    for rate in listofCurrency:
        rate = list(rate.split(","))
        add_edge(rate[0], rate[1], float(rate[2]))
        add_edge(rate[1], rate[0], 1/float(rate[2]))

def validate(listofCurrency):
    for i, line in enumerate(listofCurrency):
        if i == 0:
                rateList = line
        if i == 1:
                origin = line
        if i == 2:
                target = line
    print(listofCurrency)
    #build_graph(rateList)

    #if origin not in graph or target not in graph:
    #        return -1.0

    print(graph)

validate(question)

for i, line in enumerate(sys.stdin):
    if i == 0:
        rateList = line
    if i == 1:
        origin = line
    if i == 2:
        target = line