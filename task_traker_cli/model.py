# Функционал моего приложение / работа с бд
import datetime
import sqlite3

class Todo:
  
  def __init__(self):
    try:
      #подключение к бд и создание таблицы если есть
      self.connect = sqlite3.connect("task_traker.db")
      self.cursor = self.connect.cursor()

      self.__create_table()
      
    except sqlite3.Error as e:
      print("Ошибка при подключении к sqlite:", e)

    
  # Закрытие подключения бд
  def __close_db(self):
    self.connect.close()

  # Создание таблицы
  def __create_table(self):
    self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS todos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        status TEXT NOT NULL,
                        createdAt TEXT NOT NULL,
                        updatedAt TEXT NOT NULL
                        )
                        ''')
  
  # Добавление задач
  def insert_todo(self, description, status='todo'):

    dateNow = datetime.datetime.now().isoformat()

    sql = "INSERT INTO todos VALUES (:id, :description, :status, :createdAt, :updatedAt)"

    data = {
      'id': None,
      'description': description,
      'status': status,
      'createdAt': dateNow,
      'updatedAt': dateNow,
    }

    self.cursor.execute(sql, data)
    self.connect.commit()

    # Закрытие соединения
    self.__close_db()

  # Удаление задачи
  def delete_todo(self, id_task):
    
    self.cursor.execute("DELETE FROM todos WHERE id=:id",  {'id': id_task})
    self.connect.commit()

    self.__close_db()

  # Обновление описания задачи
  def update_todo(self, id_task, description):
    
    sql = "UPDATE todos SET description=:description, updatedAt=:updatedAt WHERE id=:id"

    data = {
      'id': id_task,
      'updatedAt': datetime.datetime.now().isoformat(), 
      'description': description
    }

    self.cursor.execute(sql, data)
    self.connect.commit()

    self.__close_db()

  # обновление статуса задачи
  def update_status_todo(self, id_task, status):

    sql = "UPDATE todos SET status=:status, updatedAt=:updatedAt WHERE id=:id"

    data = {
      'id': id_task,
      'updatedAt': datetime.datetime.now().isoformat(), 
      'status': status
    }

    self.cursor.execute(sql, data)
    self.connect.commit()

    self.__close_db()

  # Список задач по статусу или все
  def get_all_todo(self):
    self.cursor.execute("SELECT * FROM todos")
    results = self.cursor.fetchall()
    return results
  
  def get_todo_status(self, status):
    self.cursor.execute("SELECT * FROM todos WHERE status=:status", {'status': status})
    results = self.cursor.fetchall()
    return results
  
