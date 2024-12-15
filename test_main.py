import unittest
from main import filter_commits

class TestFilterCommits(unittest.TestCase):

    def test_filter_commits(self):
        commits = [
            {"hash": "a1", "message": "Fix bug", "date": "2023-03-20T10:00:00"},
            {"hash": "b2", "message": "Add feature", "date": "2023-03-21T10:00:00"},
            {"hash": "c3", "message": "Improve stability", "date": "2023-03-29T12:00:00"}
        ]

        dependencies = [
            {"parent": "a1", "child": "b2"},
            {"parent": "a1", "child": "c3"}
        ]

        before_date = "2023-03-31T23:59:59"

        filtered_commits, filtered_dependencies = filter_commits(commits, dependencies, before_date)

        self.assertEqual(len(filtered_dependencies), 2)  # Ожидаем 2 зависимости


if __name__ == "__main__":
    unittest.main()
