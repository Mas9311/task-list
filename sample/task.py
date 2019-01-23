from . import file_helper, format


def create_lists():
    my_lists = {}
    files = file_helper.get_all_files()
    for filename in files:
        my_lists[filename] = Task(filename)
    return my_lists


def return_all(my_lists):
    output = ''
    for curr_list in my_lists.values():
        output += f'{curr_list}\n'
    return output


class Task:
    def __init__(self, filename):
        self.filename = filename
        self.file_path = file_helper.get_file(filename)
        self.singular = filename.replace('_', ' ')
        if len(filename) > 1 and filename[-1] == 's':
            self.singular = filename[:-1]
        self.tasks = file_helper.read(self.file_path)

    def cap_singular(self):
        return format.capitalize_first(self.singular)

    def get_file(self):
        return format.normalize_file(self.filename)

    def add_task(self, description, index):
        self.tasks.insert(index, (index, description))
        self.reorder_numbering()

    def remove_task(self, real_index):
        self.tasks.pop(real_index)
        self.reorder_numbering()

    def rename_task(self, index, description):
        self.tasks[index] = (index + 1, description)
        self.reorder_numbering()

    def rearrange_a_task(self, first, second):
        real_first = first
        real_second = second
        task_to_move = self.tasks[real_first][1]

        self.tasks.pop(real_first)
        self.tasks.insert(real_second, (second, task_to_move))
        self.reorder_numbering()

    def reorder_numbering(self):
        for new_index in range(len(self.tasks)):
            description = self.tasks[new_index][1]
            self.tasks[new_index] = (new_index + 1, description)
        file_helper.write(self)

    def __str__(self):
        if not self.tasks:
            message = f'│ You have completed all of your {self.get_file()}! │'
            top_line = '┌' + ('─' * (len(message) - 2)) + '┐'
            bot_line = '└' + ('─' * (len(message) - 2)) + '┘'
            return f'{top_line}\n{message}\n{bot_line}'

        title = f'  ' + str(self.get_file()) + ' To Complete:  '
        left_spaces = 5
        if len(self.tasks) >= 10:
            left_spaces += 1
        line_len = max(len(title) + 2,
                       left_spaces + max([len(each_task[1]) for each_task in self.tasks]) + 4)
        top_line = '┌'
        top_line += '─' * (line_len - 2)
        top_line += '┐'
        title_line = '│'
        title_line += title
        title_line += ' ' * (line_len - len(title) - 2)
        title_line += '│'
        mid_line = '┢'
        mid_line += '━' * (line_len - 2)
        mid_line += '┪'
        tasks_output = ''
        for index in range(len(self.tasks)):
            task_output = f'┃  {self.tasks[index][0]}. {self.tasks[index][1]}'
            right_spaces = ' ' * (line_len - len(task_output) - 1)
            tasks_output += f'{task_output}{right_spaces}┃'
            if index is not len(self.tasks) - 1:
                tasks_output += '\n'
        bot_line = '┗'
        bot_line += '━' * (line_len - 2)
        bot_line += '┛'

        return(f'{top_line}\n'
               f'{title_line}\n'
               f'{mid_line}\n'
               f'{tasks_output}\n'
               f'{bot_line}')
