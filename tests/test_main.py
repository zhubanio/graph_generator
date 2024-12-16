import unittest
from main import filter_commits

class TestFilterCommits(unittest.TestCase):

    def setUp(self):
        """Настройка данных перед каждым тестом."""
        self.commits = [
            {"hash": "a1", "message": "Fix bug", "date": "2023-03-20T10:00:00"},
            {"hash": "b2", "message": "Add feature", "date": "2023-03-21T10:00:00"},
            {"hash": "c3", "message": "Improve stability", "date": "2023-03-29T12:00:00"}
        ]

        self.dependencies = [
            {"parent": "a1", "child": "b2"},
            {"parent": "a1", "child": "c3"}
        ]

        self.before_date = "2023-03-31T23:59:59"

    def test_filter_commits(self):
        """Тест фильтрации коммитов и зависимостей."""
        filtered_commits, filtered_dependencies = filter_commits(
            self.commits, self.dependencies, self.before_date
        )

        print("\nРезультаты фильтрации:")
        print(f"  Фильтрованные коммиты: {[c['hash'] for c in filtered_commits]}")
        print(f"  Фильтрованные зависимости: {filtered_dependencies}")

        # Проверяем количество зависимостей
        self.assertEqual(len(filtered_dependencies), 2, "Количество зависимостей неверное")

        # Проверяем, что все зависимости корректны
        expected_dependencies = [
            {"parent": "a1", "child": "b2"},
            {"parent": "a1", "child": "c3"}
        ]
        self.assertEqual(filtered_dependencies, expected_dependencies, "Зависимости не совпадают")


if __name__ == "__main__":
    unittest.main(verbosity=2)
