# Social Network Analysis — Viva Preparation

## 1. What is Social Network Analysis?
It is the study of relationships between entities represented as a network of nodes and edges.

## 2. What is a node?
A node (or vertex) represents an entity. In this project, a node represents a sample user.

## 3. What is an edge?
An edge represents a relationship between two nodes. The current sample uses undirected edges.

## 4. Why is this project connected to Discrete Mathematics?
It applies graph theory, sets and relations, combinatorial counting, logical inference, and feature-vector representation to a sample network.

## 5. What is the degree of a vertex?
The degree is the number of edges incident to that vertex, or the number of direct neighbors in this simple graph.

## 6. What is degree centrality?
For n > 1, normalized degree centrality is deg(v)/(n−1). It compares a node's direct connections with the maximum possible number of neighbors.

## 7. What is graph density?
Density is the number of existing edges divided by the maximum possible edges. For a simple undirected graph, density = |E|/[n(n−1)/2].

## 8. How many edges can a six-user undirected simple graph have?
C(6,2) = 6×5/2 = 15.

## 9. What is the handshake lemma?
The sum of all vertex degrees equals twice the number of edges: Σdeg(v)=2|E|. Each undirected edge contributes one degree to each endpoint.

## 10. What is a shortest path?
A path containing the fewest edges between a chosen start and target vertex. This dashboard uses breadth-first search (BFS) to find it in an unweighted graph.

## 11. What does connected mean?
A graph is connected if a path exists between every pair of vertices.

## 12. What is the difference between a directed and undirected graph?
In a directed graph, A→B need not mean B→A. In an undirected graph, A—B is symmetric.

## 13. Why use a sample dataset?
It makes the calculations easy to inspect and reproduce without collecting private or unapproved personal information.

## 14. What technologies are used?
HTML, CSS, vanilla JavaScript, SVG, and JSON. No framework, database, or API key is required.

## 15. What is the purpose of the dashboard?
It provides interactive graph visualization, node metrics, edge management, a math lab, and JSON import/export.

## 16. Does the dashboard use real social-media data?
No. It uses a synthetic illustrative network. It does not scrape or connect to a social-media platform.

## 17. What is a tree?
A tree is a connected acyclic graph. A tree with n vertices has n−1 edges.

## 18. What is an Euler path?
A path that traverses every edge exactly once.

## 19. What is a Hamilton path?
A path that visits every vertex exactly once.

## 20. What are limitations and future improvements?
Current data edits are temporary in the browser. Future work could add persistent storage, a Python/NetworkX analysis backend, community detection, directed/weighted graphs, and approved real datasets.

## Short presentation flow
1. Introduce the problem and node/edge model.
2. Explain the synthetic six-user dataset.
3. Demonstrate degree, density, and possible edges.
4. Show the shortest-path calculator and Math Lab.
5. Map the demo to the five syllabus units.
6. Explain limitations and future improvements.
