import unittest
from visualizer import generate_mermaid_graph

class TestGenerateMermaidGraph(unittest.TestCase):

    def test_generate_mermaid_graph(self):
        commits = [
            {"hash": "a1", "message": "Fix bug"},
            {"hash": "b2", "message": "Add feature"},
        ]

        dependencies = [
            {"parent": "a1", "child": "b2"},
        ]

        mermaid_content = generate_mermaid_graph(commits, dependencies)

        self.assertIn('a1["Fix bug"]', mermaid_content)
        self.assertIn('b2["Add feature"]', mermaid_content)
        self.assertIn('a1 --> b2', mermaid_content)

if __name__ == "__main__":
    unittest.main()
