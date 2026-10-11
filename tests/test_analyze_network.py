"""Unit tests for the standard-library graph analyzer."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("analyze_network", ROOT / "scripts" / "analyze_network.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class AnalyzeNetworkTests(unittest.TestCase):
    def setUp(self):
        self.names, self.edges = MODULE.load_graph(ROOT / "data" / "sample-network.json")
        self.result = MODULE.analyze(self.names, self.edges)

    def test_sample_counts(self):
        self.assertEqual(self.result["n"], 6)
        self.assertEqual(self.result["m"], 9)
        self.assertEqual(self.result["possible_edges"], 15)

    def test_density_and_average_degree(self):
        self.assertAlmostEqual(self.result["density"], 0.6)
        self.assertAlmostEqual(self.result["average_degree"], 3.0)

    def test_handshake_lemma(self):
        self.assertEqual(self.result["degree_sum"], 2 * self.result["m"])

    def test_highest_degree_tie(self):
        maximum = max(self.result["degrees"].values())
        self.assertEqual({n for n, d in self.result["degrees"].items() if d == maximum}, {"C", "E"})

    def test_connected_sample(self):
        self.assertTrue(self.result["connected"])
        self.assertEqual(len(self.result["components"]), 1)

    def test_empty_graph(self):
        result = MODULE.analyze({}, set())
        self.assertEqual(result["density"], 0)
        self.assertFalse(result["connected"])


if __name__ == "__main__":
    unittest.main()
