class Feedback:
    """Creates a border wall around the message so the user can notice messages easier.
    If the is_invalid """
    def __init__(self, is_invalid, information):
        self.is_invalid = bool(is_invalid)
        self.information = information
        self.indent = '  ' if self.is_invalid else ''
        self.width = 2 + 14 + 2
        self.vert_border_char = '*' if self.is_invalid else '║'

    def create_border_line(self, is_top):
        first_char = '*'
        last_char = '*'
        horizontal_border_char = '*'
        output = ''
        if not self.is_invalid:
            horizontal_border_char = '═'
            if is_top:
                first_char = '╔'
                last_char = '╗'
            else:
                first_char = '╚'
                last_char = '╝'
        for _ in range(self.width - 2):
            output += horizontal_border_char
        return f'{first_char}{output}{last_char}'

    def spacing(self, information_line):
        ending_spaces = ''
        num_spaces = self.width - 4 - len(information_line)
        for _ in range(num_spaces):
            ending_spaces += ' '
        return f'{self.vert_border_char} {information_line}{ending_spaces} {self.vert_border_char}'

    def __str__(self):
        information_str = f''
        padding = 6 if self.indent else 4
        if type(self.information) is list:
            self.width = max(2 + 14 + 2, max([len(each_line) for each_line in self.information]) + padding)
            for i in range(len(self.information)):
                information_str += f'{self.spacing(self.indent + self.information[i])}'
                information_str += f'\n' if i is not len(self.information)-1 else ''
        else:
            self.width = max(self.width, len(self.information) + padding)
            information_str = f'{self.spacing(self.indent + self.information)}'

        invalid_str = self.spacing('Invalid entry:') + '\n' if self.is_invalid else ''
        top_border_line = self.create_border_line(True)
        bot_border_line = self.create_border_line(False)
        output = (f'{invalid_str}'
                  f'{information_str}')

        return (f'\n{top_border_line}\n'
                f'{output}\n'
                f'{bot_border_line}\n')
