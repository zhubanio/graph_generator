import unittest
import json
from main import load_config

class TestLoadConfig(unittest.TestCase):

    def test_load_config(self):
        test_config_data = {
            "before_date": "2023-06-30",
            "output_path": "test_output.png",
            "repository": "https://github.com/test-repo"
        }
        test_file = "test_dependencies.json"

        with open(test_file, "w") as f:
            json.dump(test_config_data, f)

        config = load_config(test_file)

        self.assertEqual(config["before_date"], "2023-06-30")
        self.assertEqual(config["output_path"], "test_output.png")
        self.assertEqual(config["repository"], "https://github.com/test-repo")

if __name__ == "__main__":
    unittest.main()
