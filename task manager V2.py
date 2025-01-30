import datetime
import json

massege = """ 1-Add task to a list 
 2-Add tags 
 3-Mark task as complete
 4-View tasks 
 5-Delete task
 6-Quit """

def load_tasks(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"tasks": []}

def save_tasks(file_path, tasks):
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("What is the task:\n")
    task_info = {
        "task": task,
        "status": False,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "tags": []
    }
    tasks["tasks"].append(task_info)
    save_tasks('taskmanger_data.json', tasks)
    print('Task added. It is now in the list of tasks.')

def add_tags(tasks):
    if not tasks["tasks"]:
        print("No tasks available to add tags.")
        return
    for i, task in enumerate(tasks["tasks"]):
        print(f'{i+1}. {task["task"]} - at {task["date"]}')
    task_num = int(input("Please enter your task number or press 0 to skip: "))
    if task_num == 0 or task_num-1 >= len(tasks["tasks"]):
        print('Invalid task number.')
        return
    tags_list = input('Please enter your tags, separated by commas:\n').split(',')
    tasks["tasks"][task_num - 1]['tags'].extend(tags_list)
    save_tasks('taskmanger_data.json', tasks)

def delete_task(tasks):
    view_tasks(tasks)
    delete_num = int(input('Please enter the number of the task you want to remove, or press 0 to skip: '))
    if delete_num == 0 or delete_num-1 >= len(tasks["tasks"]):
        print('Invalid task number.')
        return
    del tasks['tasks'][delete_num-1]
    save_tasks('taskmanger_data.json', tasks)
    print("Task deleted successfully.")

def mark_task_complete(tasks):
    incompleted_tasks = [task for task in tasks["tasks"] if not task['status']]
    if not incompleted_tasks:
        print('No tasks to mark as complete.')
        return
    for i, task in enumerate(incompleted_tasks):
        print(f"{i+1}- {task['task']}")
    task_num = int(input('Enter the number of the task you completed, or press 0 to skip:\n'))
    if task_num == 0 or task_num-1 >= len(incompleted_tasks):
        print('Invalid task number.')
        return
    incompleted_tasks[task_num - 1]['status'] = True
    save_tasks('taskmanger_data.json', tasks)

def view_tasks(tasks):
    if not tasks["tasks"]:
        print('No tasks to view.')
        return
    for i, task in enumerate(tasks["tasks"]):
        status = '✔' if task["status"] else '❌'
        print(f'{i+1}. {task["task"]} {status} - added on {task["date"]} with tags: {task["tags"] if task["tags"] else "no tags"}')

def body_pro():
    tasks = load_tasks('taskmanger_data.json')
    while True:
        print(massege)
        choice = input('Enter your choice:\n')
        if choice == "1":
            add_task(tasks)
        elif choice == '2':
            add_tags(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            break
        else:
            print('Invalid choice. Please choose a number from the list.')

body_pro()
