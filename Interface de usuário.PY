# ui.py

from task_manager import TaskManager

def display_menu():
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("4. Sair")

def get_task_info():
    title = input("Título da tarefa: ")
    description = input("Descrição da tarefa: ")
    due_date = input("Data de vencimento (opcional): ")
    return title, description, due_date if due_date else None

def main():
    task_manager = TaskManager()

    while True:
        display_menu()
        choice = input("Escolha uma opção: ")

        if choice == '1':
            title, description, due_date = get_task_info()
            task_manager.add_task(title, description, due_date)
            print(f"Tarefa '{title}' adicionada com sucesso!")

        elif choice == '2':
            title = input("Título da tarefa a remover: ")
            task_manager.remove_task(title)
            print(f"Tarefa '{title}' removida com sucesso!")

        elif choice == '3':
            tasks = task_manager.list_tasks()
            if tasks:
                print("\nTarefas:")
                for task in tasks:
                    print(task)
            else:
                print("Nenhuma tarefa encontrada.")

        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
