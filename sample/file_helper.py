from . import format
import os


def get_folder():
    return os.path.join(os.getcwd(), 'my_lists')


def get_file(filename):
    return os.path.join(get_folder(), filename)


def get_all_files():
    return os.listdir(get_folder())


def create_default():
    """Creates the folder and both default files if they do not exist."""
    output = []
    if not os.path.exists(get_folder()):
        os.mkdir(get_folder())
        output.append('  * my_lists/ folder to hold all lists')
    todo_file = get_file('tasks')
    if not os.path.exists(todo_file):
        with open(todo_file, 'w') as new_file:
            new_file.close()
        output.append('  * tasks file to save all of your todo list items')
    chores_file = get_file('chores')
    if not os.path.exists(chores_file):
        with open(chores_file, 'w') as new_file:
            new_file.close()
        output.append('  * chores file to save all of your chores')
    if output:
        output.insert(0, 'Created the:')
        print(format.Feedback(False, output))


def create_new_file(filename):
    new_file_path = get_file(filename)
    if not os.path.exists(new_file_path):
        with open(new_file_path, 'w') as new_file:
            new_file.close()
        return True
    return False


def delete_file(filename):
    os.remove(get_file(filename))


def read(file_path):
    tasks = []
    with open(file_path, 'r') as task_file:
        lines = task_file.read().splitlines()
        task_file.close()
    for line in lines:
        tasks.append((len(tasks) + 1, line))
    return tasks


def write(curr_list):
    """This function is called once the user has selected to modify the current list."""
    with open(curr_list.file_path, 'w') as task_file:
        for each_task in curr_list.tasks:
            task_file.write(f'{each_task[1]}')
            if each_task is not curr_list.tasks[-1]:
                task_file.write('\n')
        task_file.close()
