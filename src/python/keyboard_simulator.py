from pynput.keyboard import Controller, Key

from src.python.stack import Stack


class Keyboard:

    def __init__(self):
        self.keyboardController = Controller()
        self.stacks = Stack()

    def send_keys(self, *args: str):
        for i in args:
            self.send_key(i)

    def send_key(self, arg: str):
        self.keyboardController.press(arg)
        self.keyboardController.release(arg)

    def send_keys_multiply(self, args):

        for i in args:
            for j in i.lower().split():
                if (not j.isalpha()) | len(j) > 1:
                    self.func_key(j)

                else:
                    self.keyboardController.press(j)
                self.stacks.push(j)
            while not self.stacks.is_empty():
                pop_key: str = self.stacks.pop()
                if (not pop_key.isalpha()) | len(pop_key) > 1:
                    self.func_key(pop_key, False)
                else:
                    self.keyboardController.release(pop_key)

    def func_key(self, key, isSend=True):
        key_map = {
            "cmd": Key.cmd,
            "option": Key.alt_l,
            "ctrl": Key.ctrl_l,
            **{f"f{i}": getattr(Key, f"f{i}") for i in range(1, 13)}
        }
        normalized_key = key.lower()
        if normalized_key in key_map:
            self.press_key(key_map[key], isSend)

    def press_key(self, key, isSend):
        if isSend:
            self.keyboardController.press(key)
        else:
            self.keyboardController.release(key)
