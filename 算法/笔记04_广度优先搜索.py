# hash table（散列表）：包含额外逻辑的数据结构，即字典

from collections import deque # 创建双端队列
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]

graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

#%% check if he is mango dealer
def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    searched = [] #记录哪些人已经测试过了
    search_que = deque()
    search_que += graph[name]
    
    while search_que:
        person = search_que.popleft()
        
        if person_is_seller(person):
            print(person + 'is mango dealer.')
            return True
        else:
            searched.append(person)
            search_que += graph[person]
    return False

print(search('you'))
