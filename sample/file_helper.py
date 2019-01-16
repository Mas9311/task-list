from . import format
import os


def get_folder():
    return os.path.join(os.getcwd(), 'my_tasks')


def get_file(filename):
    return os.path.join(get_folder(), filename)


def create():
    """Creates the folder and both files if they do not exist."""
    if not os.path.exists(get_folder()):
        os.mkdir(get_folder())
        print(format.Feedback(False, 'Created the my_tasks/ folder.'))
    todo_file = get_file('todo')
    if not os.path.exists(todo_file):
        with open(todo_file, 'w') as new_file:
            new_file.close()
        print(format.Feedback(False, 'Created the todo file.'))
    chores_file = get_file('chores')
    if not os.path.exists(chores_file):
        with open(chores_file, 'w') as new_file:
            new_file.close()
        print(format.Feedback(False, 'Created the chores file.'))


def read(file_path):
    tasks = []
    with open(file_path, 'r') as task_file:
        lines = task_file.read().splitlines()
        task_file.close()
    if not lines:
        return tasks
    for line in lines:
        tasks.append((len(tasks) + 1, line))
    return tasks


def write(my_tasks):
    """This function is called once the user has selected to modify a given value of the stock."""
    with open(my_tasks.file, 'w') as task_file:
        for each_task in my_tasks.tasks:
            task_file.write(f'{each_task[1]}\n')
        task_file.close()
    # print(format.Feedback(False, f'The {my_tasks.filename} file has been updated.'))
