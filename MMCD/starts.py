from os import system
from inspect import getsource


class UnknownModeError(Exception):
    def __init__(self):
        self.add_note('Unknown mode.')


class DelayedStart:
    def __init__(self, text=''):
        self.text = text

    def start(self, time_seconds, path1, path2):
        new_path = ''
        for i in path2:
            if i != '\\':
                new_path += i
            else:
                new_path += '\\\\'
        f = open(path1, 'w+')
        f.write('\n'.join(['from time import sleep', 'from os import system', f'sleep({time_seconds})', f'system("python {new_path}")']))
        f.close()
        f = open(path2, 'w+')
        f.write(self.text)
        f.close()
        system(f'pythonw {path1}')

    def change_text(self, text, mode='text'):
        if mode == 'text':
            self.text = text
        elif mode == 'function':
            self.text = getsource(text) + f'\n{text.__name__}()'
        else:
            raise UnknownModeError
        

class SecretStart:
    def __init__(self, commands=''):
        self.change_text(commands)
        
    def start(self, path):
        f = open(path, 'w+')
        f.write(self.text)
        f.close()

        system(f'pythonw {path}')

    def change_text(self, commands):
        if type(commands) is str:
            self.text = commands
        elif type(commands) is list:
            self.text = '\n'.join(map(str, commands))
        else:
            try:
                self.text = getsource(commands) + f'\n{commands.__name__}()'
            except TypeError:
                raise UnknownModeError