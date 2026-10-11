# NetScope — Social Network Analysis Dashboard

An interactive student capstone dashboard that applies ideas from **Discrete Mathematics** to a small social network. It follows the five units in the supplied capstone material: Logic & Proofs, Sets & Relations, Combinatorics, Algebraic Systems, and Graph Theory.

## Open the dashboard

- **Run locally:** open [index.html](index.html) in a modern browser, or open the repository in VS Code and use Live Server.
- **Hosted option:** a GitHub Pages deployment workflow is included in `.github/workflows/deploy-pages.yml`. In the repository, open **Settings → Pages**, set the build/deployment source to **GitHub Actions**, and then check the Actions tab after the next push. The published URL will appear in the workflow deployment result once GitHub Pages is enabled.

## Dashboard features

- Interactive SVG network graph; select a node to inspect its neighbors.
- Calculated node degree, normalized degree centrality, network density, average degree, connectivity, possible edges, and degree-sum check.
- User search plus add/remove sample users and connections.
- JSON dataset import and export.
- Math Lab with combinatorics calculator, Modus Ponens demonstration, feature-vector example, handshake lemma check, and shortest-path search using breadth-first search (BFS).
- Responsive layout for desktop and mobile browsers.
- Project guide with formulas, scope, assumptions, and run instructions.

## Repository structure

```text
.
├── index.html
├── data/
│   └── sample-network.json
├── docs/
│   ├── project-report.md
│   └── viva-questions.md
├── .github/
│   └── workflows/
│       └── deploy-pages.yml
└── README.md
```

## Sample dataset

The starter graph contains six synthetic users (A–F) and nine undirected edges. It is illustrative, not real social-media data.

- Vertices: 6
- Edges: 9
- Maximum possible edges: 6 × 5 / 2 = 15
- Density: 9 / 15 = 60%
- Degree sequence: A:3, B:3, C:4, D:2, E:4, F:2
- Degree sum: 18 = 2 × 9 edges
- Highest degree in this dataset: C and E (tie)

The dashboard currently models an **undirected simple graph**. It does not scrape social platforms, connect to an API, or use a backend database. Imported/edited data is temporary in the browser session; export JSON to keep a copy.

## Technologies

HTML5, CSS3, vanilla JavaScript, SVG, and JSON. No npm install, API key, or external JavaScript library is required.

## Documentation

- [Project report](docs/project-report.md)
- [Viva questions and answers](docs/viva-questions.md)
- [Sample network JSON](data/sample-network.json)

## Team

The uploaded capstone material lists **SRINITESH M, SANJITH S, and YOGESH R P**. Confirm final roles, faculty details, and the exact submission title with your team. Repository setup contributor: Sivaperumal B.

## License

No license has been specified. Add one if the project owners decide how others may reuse the code.
