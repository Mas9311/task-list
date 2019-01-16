from . import file_helper, format


class Task:
    def __init__(self, filename):
        self.filename = filename
        self.file = file_helper.get_file(filename)
        self.type_of = 'task' if filename == 'todo' else 'chore'
        self.tasks = file_helper.read(self.file)

    def get_description(self, index):
        description = self.tasks[index][1]
        return f'{description[0].upper()}{description[1:].lower()}'

    def add_task(self, description, real_index):
        self.tasks.insert(real_index, (real_index, description))
        self.reorder_numbering()

    def remove_task(self, real_index):
        self.tasks.pop(real_index)
        self.reorder_numbering()

    def is_valid_index(self, real_index):
        if real_index >= len(self.tasks) or real_index < 0:
            print(format.Feedback(True, f'\'{real_index + 1}\' is out of range.'))
            return False
        return True

    def rename_task(self, index, description):
        self.tasks[index] = (index + 1, description)

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

    def __str__(self):
        title = f'  {self.type_of[0].upper()}{self.type_of[1:]}s To Complete:  '
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
        for task in self.tasks:
            task_output = f'┃  {task[0]}. {task[1][0].upper()}{task[1][1:]}'
            right_spaces = ' ' * (line_len - len(task_output) - 1)
            tasks_output += f'{task_output}{right_spaces}┃'
            if task is not self.tasks[-1]:
                tasks_output += '\n'
        bot_line = '┗'
        bot_line += '━' * (line_len - 2)
        bot_line += '┛'

        return(f'{top_line}\n'
               f'{title_line}\n'
               f'{mid_line}\n'
               f'{tasks_output}\n'
               f'{bot_line}')
