import os
import json

try: 
    with open('TaskLogger.json','r') as tasksJson:
        tasks = json.load(tasksJson)
except FileNotFoundError:
    tasks = []

def add():
    task = input('Task Name:  ').lower()
    is_done = input('Is is already Done? Yes or No:  ').lower()
    if is_done=='yes':
        tasks.append({'name':task,
                      'status':'completed'})
        update_file()
    elif is_done=='no':
        tasks.append({'name':task,
                      'status':'pending'})
        update_file()
    else:
        print('Yes or No only')

def delete():
    taskname = input('Task Name:  ').lower()
    for i,task in tasks:
        if task['name']==taskname:
            print('Deleted:  ')
            is_deleted = tasks.pop(i)
            update_file()
            task_list()
            break
    if is_deleted:
        print('Deleted')
    else:
        print('File Not Found')

def show_command():
    print("""
        Type:
        /add -to Add a Task.
        /delete -to Remove it.
        /edit -to Edit status and name.
        /task_list/  all -to show All tasks.
        /task_list/ completed -to show Completed Tasks.
        /task_list/ pending -to show pending Tasks.
        """)

def edit():
    taskname = input('Name of the Task you want to Edit? :  ').lower()
    for task in tasks:
        if task['name']==taskname:
            edit_what = input('What would you Like to Edit: Name or Status:  ').lower()
            if edit_what == 'name': 
                edit = input('Enter:  ')
                task['name']=edit
                update_file()
            elif edit_what == 'status':
                edit = input('Enter Pending or Completed:  ').lower()
                if edit == 'pending' or edit == 'completed':
                    task['status'] = edit
                    update_file()
            else:
                print('Something Went Wrong Type /show_command for more info')
                break

def task_list():
    category = input('Sort By? All or Pending or Completed:  ').lower()
    if category == 'all':
        for task in tasks:
            print(task)
    elif category =='pending' or category == 'completed':
        for task in tasks:
            if task['status'] == category:
                print(task)
    else:
        print('Something Went Wrong or command not viable')

def update_file():
    with open('TaskLogger.json','w') as tasksJson:
        json.dump(tasks,tasksJson,indent=2)
        
cmd = {
    '/add': add,
    '/delete':delete,
    '/show_command': show_command,
    '/edit': edit,
    '/task_list': task_list
}

    
while True: 
    commands = input('Commands:  ').lower()
    if cmd.get(commands):
        cmd[commands]()
    elif commands == '/exit' or commands == '/quit':
        break
    else:
        print('Unknown Command')
        show_command()
        