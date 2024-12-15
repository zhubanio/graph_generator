import json
import os
from visualizer import generate_mermaid_graph, render_graph
os.system('chcp 65001 > nul')

def load_config(config_path):
    """Загрузка конфигурации из JSON файла."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Файл конфигурации {config_path} не найден.")
    with open(config_path, 'r') as f:
        return json.load(f)


def filter_commits(commits, dependencies, before_date):
    """Фильтрация коммитов и зависимостей до заданной даты."""
    from datetime import datetime

    # Преобразуем before_date в offset-naive
    before_date_naive = datetime.fromisoformat(before_date).replace(tzinfo=None)

    # Фильтруем коммиты по дате
    filtered_commits = [
        commit for commit in commits
        if datetime.fromisoformat(commit["date"]).replace(tzinfo=None) <= before_date_naive
    ]

    filtered_hashes = {commit["hash"] for commit in filtered_commits}

    # Оставляем зависимости только между отфильтрованными коммитами
    filtered_dependencies = [
        dep for dep in dependencies if dep["parent"] in filtered_hashes and dep["child"] in filtered_hashes
    ]

    return filtered_commits, filtered_dependencies


def main():
    """Основной метод для запуска программы."""
    config = load_config("dependencies.json")
    commits = config["commits"]
    dependencies = config["dependencies"]
    before_date = config["before_date"]
    output_path = config["output_path"]
    visualizer_path = config["visualizer_path"]

    # Фильтрация данных
    commits, dependencies = filter_commits(commits, dependencies, before_date)

    if not commits:
        print("Нет подходящих коммитов для визуализации.")
        return

    # Генерация Mermaid-графа
    mermaid_content = generate_mermaid_graph(commits, dependencies)

    # Рендеринг графа
    render_graph(mermaid_content, visualizer_path, output_path)
    print(f"Граф зависимостей сохранён в {output_path}")


if __name__ == "__main__":
    main()

