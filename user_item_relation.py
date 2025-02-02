from collections import defaultdict

class RelationshipGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_interaction(self, user, item):
        self.graph[user].append(item)
        self.graph[item].append(user)

    def dfs(self, start_node):
        visited = set()
        
        def _dfs(node):
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    _dfs(neighbor)
        
        _dfs(start_node)
        return visited

# construct the class to add user and item to the graph
user_item_relation = RelationshipGraph()
user_item_relation.add_interaction("user1", "item1")
user_item_relation.add_interaction("user1", "item2")
print(user_item_relation.dfs("user1")) 

#Output will be user1, item1, and item2. It is linking the item with user1