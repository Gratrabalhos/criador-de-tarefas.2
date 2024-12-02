# task.py

class Task:
    def __init__(self, title, description, due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date

    def __str__(self):
        due_date_str = f" (Due: {self.due_date})" if self.due_date else ""
        return f"{self.title}{due_date_str}: {self.description}"
