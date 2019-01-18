import sys
from . import task, file_helper, format


def main_menu():
    file_helper.create_default()
    my_lists = task.create_lists()
    if len(sys.argv) > 1 and sys.argv[1] == 'print':
        task.print_lists(my_lists)
        return
    while True:
        key = file_menu(my_lists)
        if not key:
            return
        else:
            edit_menu(my_lists[key])


def file_menu(my_lists):
    while True:
        menu_output = (f'Enter the desired [option] from the list below:\n'
                       f'\t[1] to Print all lists\n')
        curr_option = 1
        options = {}
        for key in my_lists:
            options[curr_option] = key
            menu_output += f'\t[{curr_option + 1}] to modify the {my_lists[key].get_file()} list\n'
            curr_option += 1

        selection = retrieve_index(len(my_lists) + 1, menu_output)
        if selection is 'return':
            return ''
        elif selection is 0:
            task.print_lists(my_lists)
            print()
        else:
            return options[selection]


def edit_menu(curr_list):
    while True:
        menu_output = ''
        additional_menu = ''
        max_range = 1
        if not curr_list.tasks:
            print(format.Feedback(False, f'You do not have any {curr_list.type_of}s to print.'))
        else:
            menu_output = f'{curr_list}\n'

        menu_output += (f'\nEnter the desired [option] from the list below:\n'
                        f'\t[1] to Add a new {curr_list.type_of}\n')
        if curr_list.tasks:
            max_range = 5
            if len(curr_list.tasks) is 1:
                additional_menu = (f'\t[2] to Rename the {curr_list.type_of}\n'
                                   f'\t[4] to Remove the {curr_list.type_of}\n'
                                   f'\t[5] to Print your {curr_list.type_of} again\n')
            if len(curr_list.tasks) > 1:
                additional_menu = (f'\t[2] to Rename a {curr_list.type_of}\n'
                                   f'\t[3] to Reorder a {curr_list.type_of}\n'
                                   f'\t[4] to Remove a {curr_list.type_of}\n'
                                   f'\t[5] to Print your {curr_list.filename} again\n')
        selection = retrieve_index(max_range, menu_output + additional_menu)
        if selection is 'return':
            return
        selection += 1
        if selection is 1:
            add_task(curr_list)
        elif selection is 2:
            rename_task(curr_list)
        elif selection is 3:
            reorder_tasks(curr_list)
        elif selection is 4:
            remove_task(curr_list)
        elif selection is 5:
            pass
        else:
            print('* Failure @67 * ', type(selection), selection)


def add_task(curr_list):
    index = 0
    len_list = len(curr_list.tasks)
    description = input(f'Enter the name of the {curr_list.type_of}\n'
                        f'  or press [Enter] to return.\n').strip().lower()
    if not description:
        return
    elif len_list:
        print()
        menu_output = (f'{curr_list}\n'
                       f'\nEnter the desired [option] from the list below:\n'
                       f'\t[1] to add it to the top\n')
        if len_list > 1:
            menu_output += '\t...\n'
        menu_output += f'\t[{len_list + 1}] to append it to the bottom\n'
        index = retrieve_index(len_list + 1, menu_output)
        if index is 'return':
            return
    curr_list.add_task(description, index)


def rename_task(curr_list):
    index = 0
    len_list = len(curr_list.tasks)
    if len_list is 0:
        print(format.Feedback(False, f'You do not have any {curr_list.type_of} to rename.'))
        return
    elif len_list > 1:
        menu_output = (f'{curr_list}\n'
                       f'\nWhat is the {curr_list.type_of} [number] to rename?\n'
                       f'  or press [Enter] to quit renaming.')
        index = retrieve_index(len_list, menu_output)
        if index is 'return':
            return
    description = input(f'What do you want to rename \'{curr_list.get_description(index)}\' to?\n'
                        f'  or press [Enter] to return').strip().lower()
    if not description:
        return
    print()
    curr_list.rename_task(index, description)


def reorder_tasks(curr_list):
    if not curr_list.tasks:
        print(format.Feedback(False, f'You do not have any {curr_list.type_of} to reorder.'))
        return
    elif len(curr_list.tasks) is 1:
        print(format.Feedback(False, f'You only have one {curr_list.type_of}, so you cannot reorder them.'))
        return
    print(f'{curr_list}\n'
          f'\nThe {curr_list.type_of} will be moved FROM the first [number] TO the second [number].\n')
    from_i = retrieve_index(len(curr_list.tasks), 'What is the first [number]?\n')
    if from_i is 'return':
        return
    to_i = retrieve_index(len(curr_list.tasks), 'What is the second [number]?\n')
    if to_i is 'return':
        return
    if from_i is to_i:
        print(format.Feedback(False, 'After countless hours of computation:'))
        return
    curr_list.rearrange_a_task(from_i, to_i)


def remove_task(curr_list):
    index = 0
    if not curr_list.tasks:
        print(format.Feedback(False, 'You do not have any tasks to remove.'))
        return
    elif len(curr_list.tasks) is 1:
        pass
    else:
        menu_output = (f'{curr_list}\n'
                       f'\nWhat [number] do you want to remove?\n')
        index = retrieve_index(len(curr_list.tasks), menu_output)
        if index is 'return':
            return
    curr_list.remove_task(index)


def retrieve_index(max_range, output=''):
    user_input = ''
    while True:
        try:
            user_input = input(f'{output + f"  or press [Enter] to quit"}\n').strip().lower()
            if not user_input:
                return 'return'
            index = int(user_input)
            if 1 <= index <= max_range:
                print()
                return index - 1
            print(format.Feedback(True, f'\'{user_input}\' must be valid number in the range [1, {max_range}]'))
        except ValueError:
            print(format.Feedback(True, f'\'{user_input}\' is not a number.'))
