#Это контроллер моего cli-app по MVC
import argparse
from .model import Todo

def main():
  
  #з1. Задаем парсер сам
  parser = argparse.ArgumentParser(prog='tasker', description="Описание списка задач в кли")
  #з2. Задаем подкоманды. Должна обязательно использоваться
  subparsers = parser.add_subparsers(dest="command", required=True, help="команды: add, list, del, upd")

  '''
  #dest - атрибут в котором будет имя команды
  required - обязательно ли указывать команду
  '''

  #3 Описание функционала
  # Добавление
  add_parser = subparsers.add_parser('add', help='Добавление новой задачи')
  add_parser.add_argument('description', type=str, help='Опишите задачу')
  add_parser.add_argument(
        "--status", choices=["todo", "in-progress", "done"], default="todo", help="статус задачи")
  '''
  description - имя перенной, где будет хранится то, что было написано
  --todo флаг позволяет задать статус задачи по желанию, но по умолчанию todo (все)
  '''

  # Удаление
  delete_parser = subparsers.add_parser('delete', help="Удаление задачи")
  delete_parser.add_argument('id', type=int, help="Для удаления введите номер задачи")

  # Обновление
  update_parser = subparsers.add_parser('update', help="Обновление задачи")
  update_parser.add_argument('id', type=int, help="Номер задачи, которую нужно обновить")
  update_parser.add_argument('description', type=str, help="Введите новое название задачи")

  # Список задач по статусу или все
  list_parser = subparsers.add_parser('list', help="Выводит список задач")
  list_parser.add_argument('--status', choices=["todo", "in-progress", "done"], default='todo', help="отображение задач по статусу")

  # обновление статуса задачи
  marking_parser = subparsers.add_parser('marking', help="Обновить статус задачи")
  marking_parser.add_argument('id', type=int, help="Номер задачи, которую нужно обновить")
  marking_parser.add_argument('status', choices=['in-progress', 'done'], help="Введите желаемый статус задачи")

  # Запуск кли-приложения
  args = parser.parse_args()
  
  if args.command == 'add':
    add_todo = Todo()
    add_todo.insert_todo(description=args.description, status=args.status)
    print(f"Задача: {args.description} успешно добавлена")
  elif args.command == 'update':
    add_todo = Todo()
    add_todo.update_todo(args.id, args.description)
    print(f"Задача с номером {args.id} обновлена: {args.description}")
  elif args.command == 'delete':
    add_todo = Todo()
    add_todo.delete_todo(args.id)
    print(f"Задача с номером {args.id} Удалена")
  elif args.command == 'marking':
    add_todo = Todo()
    add_todo.update_status_todo(args.id, args.status)
    print(f"Статус задачи с номером {args.id} обновлен: {args.status}")
  elif args.command == 'list':
    add_todo = Todo()
    if args.status == 'todo':
      res = add_todo.get_all_todo()
      for task in res:
        print(f"ID:{task[0]} | Описание: {task[1]} | Статус: {task[2]} | Дата создания: {task[3]} | Дата последнего обновления: {task[4]}")
    else:
      res = add_todo.get_todo_status(args.status)
      for task in res:
        print(f"ID:{task[0]} | Описание: {task[1]} | Статус: {task[2]} | Дата создания: {task[3]} | Дата последнего обновления: {task[4]}")


