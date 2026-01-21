# todo.py
class Task:
	def __init__(self, id, title):
		self.id = id
		self.title = title
		self.done = False

class ToDoApp:
	def __init__(self):
		self.tasks = []
		self.id_counter = 1

	def add_task(self, title):
		task = Task(self.id_counter, title)
		self.tasks.append(task)
		self.id_counter += 1
		print(f"Task added (ID: {task.id})")

	def view_tasks(self):
		for t in self.tasks:
			status = "Done" if t.done else "Pending"
			print(f"ID: {t.id}, Title: {t.title}, Status: {status}")

	def delete_task(self, id):
		self.tasks = [t for t in self.tasks if t.id != id]
		print(f"Task ID {id} deleted (if existed)")

	def mark_done(self, id):
		for t in self.tasks:
			if t.id == id:
				t.done = True
				print(f"Task ID {id} marked done")
				return

def main():
	app = ToDoApp()
	while True:
		print("\n1. Add Task, 2. View Tasks, 3. Delete Task, 4. Mark Done, 5. Exit")
		choice = input("Choose: ")
		if choice == "1":
			title = input("Title: ")
			app.add_task(title)
		elif choice == "2":
			app.view_tasks()
		elif choice == "3":
			id = int(input("Task ID: "))
			app.delete_task(id)
		elif choice == "4":
			id = int(input("Task ID: "))
			app.mark_done(id)
		elif choice == "5":
			break

if __name__ == "__main__":
	main()