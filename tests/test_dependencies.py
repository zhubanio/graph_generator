import unittest
import json
from main import load_config

class TestLoadConfig(unittest.TestCase):

    def setUp(self):
        """Настройка перед каждым тестом."""
        self.test_config_data = {
            "before_date": "2023-06-30",
            "output_path": "test_output.png",
            "repository": "https://github.com/test-repo"
        }
        self.test_file = "test_dependencies.json"

        # Создание временного конфигурационного файла
        with open(self.test_file, "w") as f:
            json.dump(self.test_config_data, f)

    def tearDown(self):
        """Очистка после тестов."""
        import os
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_config(self):
        """Тест загрузки конфигурации."""
        config = load_config(self.test_file)

        self.assertEqual(config["before_date"], "2023-06-30", "Дата не совпадает")
        self.assertEqual(config["output_path"], "test_output.png", "Путь вывода не совпадает")
        self.assertEqual(config["repository"], "https://github.com/test-repo", "URL репозитория не совпадает")
        print("\nПроверено:")
        print(f"  before_date: {config['before_date']}")
        print(f"  output_path: {config['output_path']}")
        print(f"  repository: {config['repository']}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
