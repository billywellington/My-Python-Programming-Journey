# Exercise 7: Implementing a ToDo List Class
# Question:
# Define a Python class named ToDoList to represent a simple to-do list. The ToDoList class should have:
#
# An attribute for tasks, which is a list to store the tasks in the to-do list.
# Methods named add_task(), remove_task(), and display_tasks().
# The add_task() method should add a new task to the list.
# The remove_task() method should remove a task from the list.
# The display_tasks() method should print out all the tasks in the list.

class ToDoList:
    def __init__(self, tasks):
        self.tasks = []

    # The add_task() method should add a new task to the list.
    def add_task(self, task):
        self.task = task
        self.tasks.append(self.task)
        print(f"New task has been added to you ToDoList: {self.task}")

    # The remove_task() method should remove a task from the list.
    def remove_task(self, task):
        self.task = task
        self.tasks.remove(task)
        print(f"One task has been removed from your ToDoList: {self.task}\n")

    # The display_tasks() method should print out all the tasks in the list.
    def display(self):
        print("Here's your updated ToDoList:")
        i = 0
        while i < len(self.tasks):
            print(self.tasks[i])
            i +=1

myToDoList = ToDoList("Monday_ToDoList")
myToDoList.add_task("Write article1")
myToDoList.add_task("Write article2")
myToDoList.add_task("Write article3")
myToDoList.add_task("Write article4")
myToDoList.add_task("Write article5")
myToDoList.remove_task("Write article5")
myToDoList.display()