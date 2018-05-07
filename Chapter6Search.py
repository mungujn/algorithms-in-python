from collections import deque


def getGraph():
    graph = {}
    graph['me'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []
    return graph


def personsNameEndsWith(name, last_character_in_name):
    return name[-1] == last_character_in_name


def search(graph, last_character_in_name):
    search_queue = deque()  # double ended queue
    search_queue += graph

    while search_queue:
        person = search_queue.popleft()
        if personsNameEndsWith(person, last_character_in_name):
            print person + "'s name ends with " + last_character_in_name
            return True
        else:
            search_queue += graph[person]
    return False
