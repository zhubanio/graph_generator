import unittest
from visualizer import generate_mermaid_graph

class TestGenerateMermaidGraph(unittest.TestCase):

    def setUp(self):
        """Настройка данных перед каждым тестом."""
        self.commits = [
            {"hash": "a1", "message": "Fix bug"},
            {"hash": "b2", "message": "Add feature"},
        ]
        self.dependencies = [
            {"parent": "a1", "child": "b2"},
        ]

    def test_generate_mermaid_graph(self):
        """Тест генерации графа в формате Mermaid."""
        mermaid_content = generate_mermaid_graph(self.commits, self.dependencies)

        print("\nСгенерированный Mermaid-граф:\n")
        print(mermaid_content)

        # Проверяем, что узлы корректно добавлены
        self.assertIn('a1["Fix bug"]', mermaid_content, "Узел a1 отсутствует или неверен")
        self.assertIn('b2["Add feature"]', mermaid_content, "Узел b2 отсутствует или неверен")

        # Проверяем, что зависимости корректно добавлены
        self.assertIn('a1 --> b2', mermaid_content, "Связь a1 --> b2 отсутствует или неверна")


if __name__ == "__main__":
    unittest.main(verbosity=2)

