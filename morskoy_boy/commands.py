from exceptions import UserExitException
from utils import get_input_function
from models.py import Class User
from models.py import Class Shot
from models.py import Class Ship
from models.py import Class Field


from models.py
class BaseCommand(object):
    def __init__(self, command):
        self._command = command

    @property
    def command(self):
        return self._command

    @staticmethod
    def label():
        raise NotImplemented()

    def perform(self, objects, *args, **kwargs):
        raise NotImplemented()

class ExitCommand(BaseCommand):
    @staticmethod
    def label():
        return 'exit'

    def perform(self, objects, *args, **kwargs):
        raise UserExitException('See you next time!')

class NewUserCommand(BaseCommand)
    @staticmethod
    def label():
        return 'new user'

    @staticmethod
    def _load_user_classes():

    def perform(self, objects, *args, **kwargs):
        classes = self._load_user_classes()

        print('Select UserName:')
        for index, name in enumerate(classes.keys()):
            print('{}'.format(name))

        input_function = get_input_function()
        selection = None
        return new_user

class NewFieldCommand(BaseCommand)
    @staticmethod
    def label():
        return 'new field'

    @staticmethod
    def _load_field_classes():

    def perform(self, objects, *args, **kwargs):
        classes = self._load_field_classes()

        print('Select length:')
        for index, name in enumerate(classes.keys()):
            print('{}'.format(lengt))
        print('Select high:')
        for index, name in enumerate(classes.keys()):
            print('{}'.format(high))

        input_function = get_input_function()
        selection = None
        return new_field
class NewShotCommand(BaseCommand)
    def perform(self, objects, *args, **kwargs):
        classes = self._load_shot_classes()

        print('Select x:')
        for index, name in enumerate(classes.keys()):
            print('{}'.format(x))
        print('Select y:')
        for index, name in enumerate(classes.keys()):
            print('{}'.format(y))

        input_function = get_input_function()
        selection = None
        return new_shot

class NewShipCommand(BaseCommand)

    @staticmethod
    def _load_field_classes():

    def perform(self, objects, *args, **kwargs):
        classes = self._load_field_classes()

        print('Select x1:')
        for index, name in enumerate(classes.keys()):
            print('{}'.format(x1))
        print('Select y1:')
        for index, name in enumerate(classes.keys()):
            print('{}'.format(y1))
        print('Select x2:')
        for index, name in enumerate(classes.keys()):
            print('{}'.format(x2))
        print('Select y2:')
        for index, name in enumerate(classes.keys()):
            print('{}'.format(y2))

        input_function = get_input_function()
        selection = None
        return new_field




