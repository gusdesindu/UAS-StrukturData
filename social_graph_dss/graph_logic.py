
import json
import networkx as nx
import os

class SocialGraph:
    def __init__(self, data_path=None):
        if data_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            data_path = os.path.join(base_dir, 'data', 'users.json')
        self.data_path = data_path
        self.graph = nx.DiGraph()
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
            for user, friends in data.items():
                self.graph.add_node(user)
                for friend in friends:
                    self.graph.add_edge(user, friend)
        except FileNotFoundError:
            pass

    def save_data(self):
        data = {node: list(self.graph.successors(node)) for node in self.graph.nodes}
        with open(self.data_path, 'w') as f:
            json.dump(data, f, indent=2)

    def add_user(self, user):
        self.graph.add_node(user)
        self.save_data()

    def add_relation(self, user, friend):
        self.graph.add_edge(user, friend)
        self.save_data()

    def get_users(self):
        return list(self.graph.nodes)

    def get_relations(self):
        return list(self.graph.edges)

    def bfs_path(self, source, target):
        try:
            return nx.shortest_path(self.graph, source, target)
        except nx.NetworkXNoPath:
            return []
        except nx.NodeNotFound:
            return []

    def bfs_path_detailed(self, source, target):
        """BFS path dengan detail visited nodes dan langkah-langkah"""
        from collections import deque
        
        if source not in self.graph or target not in self.graph:
            return None
        
        if source == target:
            return {
                'path': [source],
                'visited': [source],
                'path_length': 0,
                'steps': []
            }
        
        queue = deque([(source, [source])])
        visited = {source}
        parent = {source: None}
        steps = []
        
        while queue:
            node, path = queue.popleft()
            
            for neighbor in self.graph.successors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    new_path = path + [neighbor]
                    
                    steps.append({
                        'from': node,
                        'to': neighbor,
                        'current_path': ' → '.join(new_path)
                    })
                    
                    if neighbor == target:
                        return {
                            'path': new_path,
                            'visited': list(visited),
                            'path_length': len(new_path) - 1,
                            'steps': steps
                        }
                    
                    queue.append((neighbor, new_path))
        
        return None

    def recommend_friends(self, user):
        if user not in self.graph:
            return []
        friends = set(self.graph.successors(user))
        recommendations = set()
        for f in friends:
            recommendations.update(set(self.graph.successors(f)))
        recommendations -= friends
        recommendations.discard(user)
        return list(recommendations)

    def most_popular_users(self, top_n=3):
        degree = self.graph.in_degree()
        sorted_users = sorted(degree, key=lambda x: x[1], reverse=True)
        return sorted_users[:top_n]
