# Social Network Analysis Dashboard — Project Report

## 1. Project title
**NetScope: Interactive Social Network Analysis using Discrete Mathematics**

## 2. Problem statement
Social networks can be viewed as mathematical systems of users, relationships, rules, and connections. It can be difficult to understand who has the most direct connections, how many relationships are possible, whether users can reach one another through paths, and how graph concepts describe a network. This project provides an interactive, small-scale demonstration of those ideas.

## 3. Objectives
- Model users as vertices and relationships as edges.
- Calculate node degree, degree centrality, density, average degree, and possible edges.
- Explore graph connectivity and shortest paths.
- Demonstrate selected syllabus concepts from all five Discrete Mathematics units.
- Provide an interactive dashboard for learning and presentation.

## 4. Scope and assumptions
- The included network is synthetic and illustrative, not data from real people.
- The current model is a simple undirected graph: an edge A—B represents a symmetric relationship.
- No external social network is scraped or connected.
- Data edits and imports are held in the current browser session; refresh returns to the built-in sample.
- The static dashboard does not include a server, user login, cloud database, or persistent multi-user storage.

## 5. Dataset
The sample contains six vertices: A, B, C, D, E, F. It includes nine undirected edges:
(A,B), (A,C), (A,E), (B,C), (B,D), (C,E), (D,E), (E,F), (C,F).

For n = 6 vertices, the maximum possible edges in a simple undirected graph are:

C(n,2) = n(n−1)/2 = (6×5)/2 = 15

The sample density is 9/15 = 0.60 (60%). The degree sequence is A:3, B:3, C:4, D:2, E:4, F:2. The degree sum is 18, which equals 2 × 9 edges and verifies the handshake lemma. C and E tie for the highest degree in this illustrative dataset. These values are calculated from the edge list above.

## 6. Mapping to the five syllabus units

### Unit I — Logic and proofs
The Math Lab demonstrates Modus Ponens: from p → q and p, infer q. Example: if a defined network rule says “if A follows B, then q,” and the premise is true, q can be inferred. The dashboard's logic widget is a teaching illustration; the sample graph itself is undirected.

### Unit II — Sets and relations
The vertex set U contains all user IDs, and E is the set of undirected edges. A directed follow relationship would require ordered pairs and should not be confused with the undirected model in this prototype. Partial orders and lattices are syllabus concepts, but are not inferred from ordinary social connections without an appropriate ordering relation.

### Unit III — Combinatorics
For n users, the number of unique pairwise connections in a simple undirected graph is n(n−1)/2 = C(n,2). The calculator lets the user change n and view the result.

### Unit IV — Algebraic systems and vectors
The dashboard includes an illustrative feature vector [friends, groups, posts]. The values are entered manually and do not describe measured behavior. Group axioms, homomorphisms, and Lagrange's theorem are theoretical syllabus topics; the demo does not claim the social graph is a group.

### Unit V — Graph theory
The network graph shows vertices and edges. The dashboard calculates degree, normalized degree centrality, density, average degree, connectivity, and shortest paths. It verifies the handshake lemma. Euler paths, Hamilton paths, trees, and graph isomorphism can be added as extended exercises.

## 7. Methodology
1. Define the sample vertex and edge sets.
2. Build adjacency lists from the edge list.
3. Calculate degree and graph summary metrics.
4. Use breadth-first search (BFS) to find shortest paths.
5. Display the graph and computed results.
6. Interpret the results in relation to the syllabus.

## 8. Technology
- HTML5 for page structure.
- CSS3 for responsive layout and visual styling.
- Vanilla JavaScript for graph calculations, interactions, validation, import/export, and SVG rendering.
- JSON for the sample dataset.
- GitHub for version control and source hosting.

The dashboard requires no package installation or API key.

## 9. How to run
1. Download or clone this repository.
2. Open index.html in a modern browser, or use VS Code Live Server.
3. Select Network graph to inspect nodes.
4. Select Users & edges to search, add/remove demo users and relationships, or import JSON.
5. Select Math lab to try combinatorics, logic, vector, and shortest-path examples.
6. Use Export data to save the current dataset as JSON.

## 10. Testing checklist
- [ ] Dashboard opens without a server or API key.
- [ ] The overview displays the expected six users and nine edges.
- [ ] Degree sum equals twice the number of edges.
- [ ] Network nodes can be selected with mouse or keyboard.
- [ ] Shortest path is found for connected nodes; unreachable nodes are reported.
- [ ] Adding/removing a user updates metrics and graph.
- [ ] Adding/removing an edge updates degree and density.
- [ ] Export creates a JSON file.
- [ ] Invalid JSON import is rejected with a clear message.
- [ ] Layout remains usable on a phone-sized viewport.

## 11. Limitations and future work
Future extensions could include a Python/NetworkX analysis module, community detection, CSV import, directed and weighted edges, a backend database, authentication, persistent datasets, and comparisons between multiple networks. Real-world data use would require suitable permission, privacy protection, and clear definitions of the relationships being studied.

## 12. Team
The uploaded capstone material lists **SRINITESH M, SANJITH S, and YOGESH R P**. Confirm each member's contribution and any faculty details before final submission. Repository setup contributor: Sivaperumal B.

## 13. Conclusion
The project demonstrates how a social network can be modelled and examined using mathematical concepts. The dashboard turns a small sample graph into an interactive learning tool and makes its assumptions and calculations visible.
