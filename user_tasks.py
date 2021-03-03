def user_tasks(current_user):
    while True:
        choice = input('Select menu item:\n'
                       '1 - view all tasks\n'
                       '2 - add new task\n'
                       '3 - update task\n'
                       '4 - delete task\n'
                       'any for exit')
        if choice == '1':
            temp = current_user.get_user_tasks()
            for i in temp.keys():
                print(f'{i} - {temp[i]}')
        elif choice == '2':
            add_task(current_user)
        elif choice == '3':
            update_task(current_user)
        elif choice == '4':
            delete_task(current_user)
        else:
            return current_user.get_user_data()


def ask_task_param():
    task_name = input('Enter task name')
    task_description = input('Enter task description')
    date = input('Enter date of completion')
    task_priority = input('Enter task priority')
    task_param = {'task_name': task_name,
                  'task_description': task_description,
                  'completion_date': date,
                  'task_priority': task_priority}
    return task_param


def add_task(current_user):
    task_param = ask_task_param()
    current_user.set_task(task_param)


def update_task(current_user):
    choice = input('Select task number: ')
    user_tasks = current_user.get_user_tasks()
    if choice in user_tasks.keys():
        task_param = ask_task_param()
        current_user.update_task(choice, task_param)
    else:
        print('Task number is incorrect')


def delete_task(current_user):
    choice = input('Select task number: ')
    user_tasks = current_user.get_user_tasks()
    if choice in user_tasks.keys():
        current_user.delete_task(choice)
        print(f'Task {choice} deleted')
    else:
        print('Task number is incorrect')
