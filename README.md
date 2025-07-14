# CLI для отслеживания задач

Интерфейс командной строки Task Tracker позволяет отслеживать задачи прямо из терминала. Вы можете добавлять, удалять, обновлять и просматривать списки задач.

- Стэк: py3.13, sqlite, argparse

# Установка
Клонируйте этот репозиторий на свой локальный компьютер:
- git clone https://github.com/EnderIO1710/taskCLI.git
- cd task_tracker_cli

# Запуск:
- python -m task_traker_cli <command> <flag>


# Использование
Для взаимодействия с Task Tracker CLI можно использовать следующие команды:

add: Добавить новую задачу

- python -m task_traker_cli add [description] --status <status>

* status необязателен, по умолчанию todo. Принимает значения: todo, done, in-progress

list: Список всех задач
- python -m task_traker_cli list

list: Список всех задач по статусу
- python -m task_traker_cli list --status <status>

update: Обновить задачу
- python -m task_traker_cli update <id> <description>

mark: изменить статус задачи
- python -m task_traker_cli marking <id> <status>

delete: Удалить задачу
- python -m task_traker_cli delete <id>

