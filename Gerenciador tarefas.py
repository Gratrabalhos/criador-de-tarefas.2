# task_manager.py

import json
from task import Task

class TaskManager:
    def __init__(self, data_file='tasks_data.json'):
        self.data_file = data_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.data_file, 'r') as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.data_file, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file, indent=4)

    def add_task(self, title, description, due_date=None):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]
        self.save_tasks()

    def list_tasks(self):
        return self.tasks
