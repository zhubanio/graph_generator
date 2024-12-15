import os
import subprocess


def generate_mermaid_graph(commits, dependencies):
    """Генерация графа зависимостей в формате Mermaid."""

    def escape_mermaid_text(text):
        """Экранирование и обработка текста для Mermaid."""
        return text.replace('"', "'").replace("\n", " ")

    graph_lines = ["graph TD"]
    commit_dict = {commit["hash"]: escape_mermaid_text(commit["message"]) for commit in commits}

    # Добавляем все узлы коммитов (даже если они не участвуют в зависимостях)
    for commit_hash, commit_message in commit_dict.items():
        graph_lines.append(f'{commit_hash}["{commit_message}"]')

    # Добавляем связи на основе зависимостей
    for dep in dependencies:
        parent = dep["parent"]
        child = dep["child"]
        graph_lines.append(f'{parent} --> {child}')

    return "\n".join(graph_lines)


def render_graph(mermaid_content, visualizer_path, output_path):
    """Рендеринг графа в изображение."""
    mermaid_file = "graph.mmd"

    # Записываем содержимое в файл graph.mmd
    with open(mermaid_file, 'w') as f:
        f.write(mermaid_content)

    command = [visualizer_path, "-i", mermaid_file, "-o", output_path]

    # Добавляем PATH для subprocess
    env = os.environ.copy()
    env["PATH"] += os.pathsep + r"C:\Program Files\nodejs"

    try:
        subprocess.run(command, check=True, env=env)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка рендеринга: {e}")
    finally:
        if os.path.exists(mermaid_file):
            os.remove(mermaid_file)

