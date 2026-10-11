# Student Guide

Welcome to NetScope! This guide explains where to find each part of the project and how to try the analysis.

## Folder map

- `index.html` — dashboard page (the starting point).
- `assets/css/dashboard.css` — colors, layout, responsive styling.
- `assets/js/dashboard.js` — dashboard interactions and browser-side graph calculations.
- `data/sample-network.json` — complete starter dataset with user names and edges.
- `data/sample-network.csv` — edge list for spreadsheet/Python analysis.
- `scripts/analyze_network.py` — command-line analysis, including degree, density, components, betweenness and closeness centrality.
- `tests/test_analyze_network.py` — automated checks for core calculations.
- `docs/project-report.md` — report suitable for adapting to your course submission.
- `docs/viva-questions.md` — viva revision.
- `.github/workflows/deploy-pages.yml` — GitHub Pages deployment workflow.

## Run the dashboard

1. Download the repository or clone it.
2. Open `index.html` in a modern browser. VS Code Live Server is optional.
3. Use Overview, Network graph, Users & edges, Math lab, and Project guide.
4. Export your edited graph as JSON. The browser demo does not permanently save edits.

## Run Python analysis (optional)

Python 3.10 or later is recommended. No third-party packages are required.

```bash
python scripts/analyze_network.py
python scripts/analyze_network.py data/sample-network.csv
python -m unittest discover -s tests -v
```

The Python report calculates normalized degree, betweenness and closeness centrality, density, average degree, connected components, and the handshake lemma check.

## Data format

JSON format: `users` is a list of objects with `id` and `name`; `edges` is a list of two-item arrays, for example `["A", "B"]`.

CSV format: one undirected edge per row, with headers `source,target`. The CSV analyzer infers nodes from the endpoints. The dashboard's built-in JSON import is separate from the Python CSV input.

## Suggested student learning path

1. Change one edge and predict which degrees will change.
2. Calculate possible edges by hand using `n(n-1)/2`.
3. Check the density and handshake lemma in both dashboard and Python output.
4. Compare degree centrality with betweenness and closeness.
5. Remove an edge that acts as a bridge and observe whether the graph becomes disconnected.
6. Try a new small graph and write down what each metric can and cannot tell you.

## Important assumptions

This is a synthetic, undirected, unweighted graph. Centrality describes mathematical structure; it does not prove that a real person is influential. Use consented, privacy-safe data if the project is extended to real-world research.
