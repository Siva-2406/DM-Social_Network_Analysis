"""Analyze an undirected social network using only Python's standard library.

Run:
    python scripts/analyze_network.py
    python scripts/analyze_network.py data/sample-network.json
    python scripts/analyze_network.py data/sample-network.csv
"""
from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict, deque
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "data" / "sample-network.json"


def load_graph(path: Path) -> tuple[dict[str, str], set[tuple[str, str]]]:
    """Return {node_id: display_name} and normalized undirected edges."""
    if path.suffix.lower() == ".csv":
        names: dict[str, str] = {}
        edges: set[tuple[str, str]] = set()
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            required = {"source", "target"}
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                raise ValueError("CSV must include source,target columns.")
            for row in reader:
                a, b = row["source"].strip(), row["target"].strip()
                if not a or not b:
                    raise ValueError("Edge endpoints cannot be empty.")
                if a == b:
                    raise ValueError(f"Self-loops are not supported: {a}")
                names.setdefault(a, a)
                names.setdefault(b, b)
                edges.add(tuple(sorted((a, b))))
        return names, edges

    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw.get("users"), list) or not isinstance(raw.get("edges"), list):
        raise ValueError("JSON must contain users[] and edges[].")
    names = {}
    for user in raw["users"]:
        node_id = str(user.get("id", "")).strip()
        if not node_id or node_id in names:
            raise ValueError("User IDs must be unique and non-empty.")
        names[node_id] = str(user.get("name") or node_id)
    edges = set()
    for edge in raw["edges"]:
        if not isinstance(edge, list) or len(edge) != 2:
            raise ValueError("Each JSON edge must be a two-item array.")
        a, b = map(str, edge)
        if a == b or a not in names or b not in names:
            raise ValueError(f"Invalid edge endpoints: {edge}")
        edges.add(tuple(sorted((a, b))))
    return names, edges


def analyze(names: dict[str, str], edges: set[tuple[str, str]]) -> dict:
    """Compute common graph measures without third-party packages."""
    nodes = sorted(names)
    adjacency = {node: set() for node in nodes}
    for a, b in edges:
        if a not in adjacency or b not in adjacency:
            raise ValueError(f"Edge references unknown node: {(a, b)}")
        adjacency[a].add(b)
        adjacency[b].add(a)

    n, m = len(nodes), len(edges)
    possible = n * (n - 1) // 2
    degrees = {node: len(adjacency[node]) for node in nodes}

    # BFS from each node computes shortest-path distances and components.
    distances = {}
    components = []
    unseen = set(nodes)
    while unseen:
        start = min(unseen)
        queue = deque([start])
        dist = {start: 0}
        while queue:
            current = queue.popleft()
            for neighbor in sorted(adjacency[current]):
                if neighbor not in dist:
                    dist[neighbor] = dist[current] + 1
                    queue.append(neighbor)
        component = sorted(dist)
        components.append(component)
        unseen.difference_update(component)
        distances[start] = dist

    # Brandes algorithm for betweenness centrality in an unweighted graph.
    betweenness = dict.fromkeys(nodes, 0.0)
    for source in nodes:
        stack = []
        predecessors = {v: [] for v in nodes}
        sigma = dict.fromkeys(nodes, 0.0)
        sigma[source] = 1.0
        dist = dict.fromkeys(nodes, -1)
        dist[source] = 0
        queue = deque([source])
        while queue:
            v = queue.popleft()
            stack.append(v)
            for w in adjacency[v]:
                if dist[w] < 0:
                    queue.append(w)
                    dist[w] = dist[v] + 1
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    predecessors[w].append(v)
        dependency = dict.fromkeys(nodes, 0.0)
        while stack:
            w = stack.pop()
            for v in predecessors[w]:
                if sigma[w]:
                    dependency[v] += (sigma[v] / sigma[w]) * (1 + dependency[w])
            if w != source:
                betweenness[w] += dependency[w]
    # Undirected normalization to [0, 1].
    scale = ((n - 1) * (n - 2) / 2) if n > 2 else 0
    betweenness = {node: (value / (2 * scale) if scale else 0.0)
                   for node, value in betweenness.items()}

    closeness = {}
    for node in nodes:
        queue = deque([node])
        dist = {node: 0}
        while queue:
            current = queue.popleft()
            for neighbor in adjacency[current]:
                if neighbor not in dist:
                    dist[neighbor] = dist[current] + 1
                    queue.append(neighbor)
        total = sum(dist.values())
        reachable = len(dist) - 1
        closeness[node] = (reachable / total * reachable / (n - 1)
                           if total and n > 1 else 0.0)

    return {
        "nodes": nodes, "edges": sorted(edges), "adjacency": adjacency,
        "degrees": degrees, "n": n, "m": m, "possible_edges": possible,
        "density": m / possible if possible else 0.0,
        "average_degree": (2 * m / n if n else 0.0),
        "degree_sum": sum(degrees.values()), "components": components,
        "connected": n > 0 and len(components) == 1,
        "betweenness": betweenness, "closeness": closeness,
    }


def print_report(names: dict[str, str], result: dict) -> None:
    print("\nNETSCOPE | SOCIAL NETWORK ANALYSIS")
    print("=" * 44)
    print(f"Vertices: {result['n']} | Edges: {result['m']}")
    print(f"Possible edges: {result['possible_edges']}")
    print(f"Density: {result['density']:.1%}")
    print(f"Average degree: {result['average_degree']:.2f}")
    print(f"Degree sum check: {result['degree_sum']} = {2 * result['m']} "
          f"({'PASS' if result['degree_sum'] == 2 * result['m'] else 'FAIL'})")
    print(f"Connected: {'Yes' if result['connected'] else 'No'}")
    print(f"Connected components: {len(result['components'])}")
    print("\nNODE METRICS")
    print(f"{'ID':<8}{'NAME':<18}{'DEGREE':>8}{'DEGREE C.':>12}"
          f"{'BETWEEN.':>12}{'CLOSENESS':>12}")
    n = result["n"]
    for node in result["nodes"]:
        degree_c = result["degrees"][node] / (n - 1) if n > 1 else 0
        print(f"{node:<8}{names[node][:17]:<18}{result['degrees'][node]:>8}"
              f"{degree_c:>12.3f}{result['betweenness'][node]:>12.3f}"
              f"{result['closeness'][node]:>12.3f}")
    hubs = [node for node in result["nodes"]
            if result["degrees"][node] == max(result["degrees"].values(), default=0)]
    print("\nHighest degree: " + (", ".join(hubs) if hubs else "None"))
    print("Note: betweenness/closeness are normalized illustrative graph metrics.")


def main() -> int:
    path = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else DEFAULT_DATA
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()
    try:
        names, edges = load_graph(path)
        result = analyze(names, edges)
        print_report(names, result)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
