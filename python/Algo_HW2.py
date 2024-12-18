#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: MEGN CHIA LEE


# Helper class for Union-Find data structure
#To begine with, every node become their own parent node 
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
#Use patb compression to find the root
    def find(self, u):
        if self.parent[u] != u: #self.parent[u] is a parent of u
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]#if it's root then parent must be theirsielve
#small tree merge into big tree
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u #root_u become root_v parent
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Greedy clustering using Kruskal's algorithm
def greedy_clustering_kruskal(distance_matrix, k):
    n = len(distance_matrix)  # Number of nodes
    edges = []

    # Create a list of all edges with their distances
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((distance_matrix[i][j], i, j))
    
    #edges by weight (distance) in ascending order
    edges.sort()

    # Initialize Union-Find for the nodes
    uf = UnionFind(n)
    clusters = {i: [i] for i in range(n)}  # Initially each node is its own cluster
    #if n =4 clusters = {0: [0], 1: [1], 2: [2], 3: [3]} in originally
    num_clusters = n  # Start with n clusters

    #Iterate through edges and join nodes until we have k clusters
    for dist, u, v in edges:
        root_u = uf.find(u)
        root_v = uf.find(v)
        
        if root_u != root_v:
            # Merge the clusters using the latest root values
            uf.union(u, v)
            
            # After union, find the new root to merge into correct cluster
            new_root = uf.find(u)
            #if true then old = v else old = u
            old_root = root_v if new_root == root_u else root_u
            
            # Merge the two clusters into the new root
            clusters[new_root].extend(clusters[old_root])
            del clusters[old_root]  # Delete the old cluster

            # Debug: Print clusters after each merge
            print(f"After merging {u} and {v}: {clusters}")

            # Decrease the number of clusters
            num_clusters -= 1

            # Stop when we reach k clusters
            if num_clusters == k:
                break

    # Return the final clusters
    return list(clusters.values())

# Use this input
distance_matrix = [
    [0, 38, 17, 28, 88, 59, 13],
    [38, 0, 52, 49, 83, 91, 59],
    [17, 52, 0, 46, 34, 77, 80],
    [28, 49, 46, 0, 5, 53, 62],
    [88, 83, 34, 5, 0, 43, 33],
    [59, 91, 77, 53, 43, 0, 27],
    [13, 59, 80, 62, 33, 27, 0]
]

# Set k=2 for number of clusters
k = 2
clusters = greedy_clustering_kruskal(distance_matrix, k)

# Print the resulting clusters
print("Resulting Clusters:", clusters)
