**Graph Dependency Visualizer** — это CLI-инструмент для визуализации графа зависимостей коммитов в git-репозитории. Программа использует формат Mermaid для описания графа и сохраняет его в формате PNG.

2-я работа по конфигурационному управлению студента Матюхи Егора Алексеевича ИКБО-42-23 РТУ МИРЭА

Для анализа коммитов был выбран тестовый репозиторий https://github.com/torvalds/test-tlb

# Graph Dependency Visualizer

##  Требования

- Python 3.9+
- Node.js (для работы с Mermaid CLI)

##  Установка

1. Клонируйте репозиторий на свой локальный компьютер:
   ```bash
   git clone https://github.com/zhubanio/graph_generator.git
зайдите в директорию  
  
    cd graph_generator

2. Убедитесь, что у вас установлен Python 3. Вы можете скачать его с официального сайта: https://www.python.org/downloads/.

3. Установите зависимости:

    ```bash
    python -m venv .venv
    .venv\Scripts\activate      # Для Windows

4. Убедитесь, что Node.js и Mermaid CLI установлены:
   ```bash
    npm install -g @mermaid-js/mermaid-cli


3. Запустите эмулятор:
   ```bash
    python main.py
      
  Изображение графа будет соединено в рабочей директории с названием dependencies_graph.png
  
    start dependencies_graph.png

## Тестирование
Для выполнения тестов, необходимо использовать модуль unittest.

Тесты можно найти в папке tests. Чтобы запустить тесты, используйте команду:

       python -m unittest discover tests/
       
## Структура проекта


      vfs-emulator/
      │
      ├── tests/
      |   ├── test_dependencies.py
      |   ├── test_main.py
      |   └── test_visualizer.py
      ├── .gitignore
      ├── LICENSE
      ├── main.py         
      ├── visualizer.py   
      ├── dependencies.json
      └── README.md        

## Лицензия
Этот проект лицензирован под MIT License.
