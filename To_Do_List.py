class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task has been deleted successfully!")
        else:
            print("Please provide a valid task index!")

    def mark_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print("Congratulations! You have successfully accomplished the task.")
        else:
            print("Oops! An error occurred. Provide a valid index")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i + 1}. {task['task']} - {status}")

def main():
    to_do_list = ToDoList()

    while True:
        print("\n**** To-Do List Menu ****")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter your task here: ")
            to_do_list.add_task(task)
            print("Task has been added successfully!")

        elif choice == "2":
            index = int(input("Enter index of the task you wish to delete: ")) - 1
            to_do_list.delete_task(index)

        elif choice == "3":
            index = int(input("Enter the task index to mark as completed: ")) - 1
            to_do_list.mark_as_completed(index)

        elif choice == "4":
            to_do_list.show_tasks()

        elif choice == "5":
            print("Exiting the to-do list application. GoodBye! ")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
