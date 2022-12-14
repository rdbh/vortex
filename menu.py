
import os


class Menu(object):
    def __init__(self, options=None, title=None, message=None, prompt=">>>",
                 refresh=lambda: None, auto_clear=True):
        if options is None:
            options = []
        self.options = None
        self.title = None
        self.is_title_enabled = None
        self.message = None
        self.is_message_enabled = None
        self.refresh = None
        self.prompt = None
        self.is_open = None
        self.auto_clear = auto_clear

        self.set_options(options)
        self.set_title(title)
        self.set_title_enabled(title is not None)
        self.set_message(message)
        self.set_message_enabled(message is not None)
        self.set_prompt(prompt)
        self.set_refresh(refresh)

    def set_options(self, options):
        original = self.options
        self.options = []
        try:
            for option in options:
                if not isinstance(option, tuple):
                    raise TypeError(option, "option is not a tuple")
                if len(option) < 2:
                    raise ValueError(option, "option is missing a handler")
                kwargs = option[2] if len(option) == 3 else {}
                self.add_option(option[0], option[1], kwargs)
        except (TypeError, ValueError) as e:
            self.options = original
            raise e

    def set_title(self, title):
        self.title = title

    def set_title_enabled(self, is_enabled):
        self.is_title_enabled = is_enabled

    def set_message(self, message):
        self.message = message

    def set_message_enabled(self, is_enabled):
        self.is_message_enabled = is_enabled

    def set_prompt(self, prompt):
        self.prompt = prompt

    def set_refresh(self, refresh):
        if not callable(refresh):
            raise TypeError(refresh, "refresh is not callable")
        self.refresh = refresh

    def add_option(self, name, handler, kwargs):
        if not callable(handler):
            raise TypeError(handler, "handler is not callable")
        self.options += [(name, handler, kwargs)]

    # open the menu
    def open(self):
        self.is_open = True
        while self.is_open:
            self.refresh()
            func = self.input()
            if func == Menu.CLOSE:
                func = self.close
            print()
            func()

    def close(self):
        self.is_open = False

    # clear the screen
    # show the options
    def show(self):
        if self.auto_clear:
            os.system('cls' if os.name == 'nt' else 'clear')
        if self.is_title_enabled:
            print(self.title)
            print()
        if self.is_message_enabled:
            print(self.message)
            print()
        for (index, option) in enumerate(self.options):
            print(str(index + 1) + ". " + option[0])
        print()

    # show the menu
    # get the option index from the input
    # return the corresponding option handler
    def input(self):
        if len(self.options) == 0:
            return Menu.CLOSE
        try:
            self.show()
            index = int(input(self.prompt + " ")) - 1
            option = self.options[index]
            handler = option[1]
            if handler == Menu.CLOSE:
                return Menu.CLOSE
            kwargs = option[2]
            return lambda: handler(**kwargs)
        except (ValueError, IndexError):
            return self.input()

    def CLOSE(self):
        pass