#program for to-do list
print("this is a task list")
print("enter your tasks one by one, and type 'done' when you are finished")
tasks = []
while True:
        task = input("what task do you want to add to your list? ")
        if task == "done":
            break
        tasks.append(task)
print(f"your task list is: {tasks}")
