from . import task, file_helper, format


def main_menu():
    file_helper.create()
    while True:
        file = file_menu()
        if not file:
            return
        my_tasks = task.Task(file)
        edit_menu(my_tasks)


def file_menu():
    while True:
        selection = input('Enter the desired [option] from the list below:\n'
                          '\t[1] for Chores list\n'
                          '\t[2] for Todo list\n'
                          '  or press [Enter] to quit.\n').strip()
        print('', end='\n')
        if not selection:
            return ''
        elif selection[0] is '1':
            return 'chores'
        elif selection[0] is '2':
            return 'todo'
        else:
            print(format.Feedback(True, f'\'{selection}\' is not a valid [option].'))


def edit_menu(my_tasks):
    while True:
        if not my_tasks.tasks:
            print(format.Feedback(False, f'You do not have any {my_tasks.type_of}s to print.'))
        else:
            print(my_tasks)
        selection = input(f'\nEnter the desired [option] from the list below:\n'
                          f'\t[1] to Add a new {my_tasks.type_of}\n'
                          f'\t[2] to Rename a {my_tasks.type_of}\n'
                          f'\t[3] to Reorder a {my_tasks.type_of}\n'
                          f'\t[4] to Remove a {my_tasks.type_of}\n'
                          f'\t[5] to Print your {my_tasks.type_of}s\n'
                          f'  or press [Enter] to return.\n').strip().lower()
        print('', end='\n')
        if not selection:
            return
        elif selection[0] is '1':
            add_task(my_tasks)
        elif selection[0] is '2':
            rename_task(my_tasks)
        elif selection[0] is '3':
            reorder_tasks(my_tasks)
        elif selection[0] is '4':
            remove_task(my_tasks)
        elif selection[0] is '5':
            pass
        else:
            print(format.Feedback(True, f'\'{selection}\' is not a valid [option].'))


def add_task(my_tasks):
    description = input(f'Enter the name of the {my_tasks.type_of}\n'
                        f'  or press [Enter] to return.\n').strip().lower()
    print('', end='\n')
    if not description:
        return
    elif not my_tasks.tasks:
        my_tasks.add_task(description, 0)
        file_helper.write(my_tasks)
        return
    else:
        print(f'{my_tasks}')
        while True:
            user_input = input(f'Enter the desired [option] from the list below:\n'
                               f'\t[1] to add it to the top\n'
                               f'\t[{len(my_tasks.tasks) + 1}] to append it to the bottom\n'
                               f'  or press [Enter] to quit adding \'{description}\'.\n').strip().lower()
            if not user_input:
                return
            try:
                real_index = int(user_input) - 1
                print(real_index)
                if 0 <= real_index <= len(my_tasks.tasks):
                    my_tasks.add_task(description, real_index)
                    file_helper.write(my_tasks)
                    return
                else:
                    print(format.Feedback(True, f'\'{user_input}\' is not a number in the stated range.'))
            except ValueError:
                print(format.Feedback(True, f'\'{user_input}\' is not a valid number.'))


def rename_task(my_tasks):
    if not my_tasks.tasks:
        print(format.Feedback(False, f'You do not have any {my_tasks.type_of} to rename.'))
        return
    print(f'{my_tasks}\n')
    index = retrieve_index(my_tasks, f'What is the {my_tasks.type_of} [number] to rename?') - 1
    description = input(f'What do you want to rename \'{my_tasks.get_description(index)}\' to?\n').strip().lower()
    my_tasks.rename_task(index, description)
    file_helper.write(my_tasks)


def reorder_tasks(my_tasks):
    if not my_tasks.tasks:
        print(format.Feedback(False, f'You do not have any {my_tasks.type_of} to reorder.'))
        return
    elif len(my_tasks.tasks) is 1:
        print(format.Feedback(False, f'You only have one {my_tasks.type_of}, so you cannot reorder them.'))
        return
    print(f'{my_tasks}\n'
          f'\nThe {my_tasks.type_of} will be moved FROM the first [number] TO the second [number]')
    first_index = retrieve_index(my_tasks, 'What is the first [number]?') - 1
    second_index = retrieve_index(my_tasks, 'What is the second [number]?') - 1
    if first_index is second_index:
        print(format.Feedback(False, ['After countless hours of computation,'
                                      '\tI present to thee:']))
    else:
        my_tasks.rearrange_a_task(first_index, second_index)
        file_helper.write(my_tasks)


def retrieve_index(my_tasks, information):
    while True:
        user_input = ''
        try:
            user_input = input(f'{information}\n').strip()
            index = int(user_input)
            if my_tasks.is_valid_index(index - 1):
                return index
        except ValueError:
            print(format.Feedback(True, f'\'{user_input}\' is not a number.'))


def remove_task(my_tasks):
    if not my_tasks.tasks:
        print(format.Feedback(False, 'You do not have any tasks to remove.'))
    else:
        while True:
            index = input(f'{my_tasks}\n'
                          f'\nWhat number do you want to remove?\n').strip()
            try:
                real_index = int(index) - 1
                if my_tasks.is_valid_index(real_index):
                    my_tasks.remove_task(real_index)
                    file_helper.write(my_tasks)
                    return
                else:
                    pass
            except ValueError:
                print(format.Feedback(True, f'\'{index}\' is not a valid number.'))
