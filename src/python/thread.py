import threading


class TimerThread(threading.Thread):
    def __init__(self, interval, callback):
        super().__init__()
        self.interval = interval
        self.callback = callback
        self.flag = threading.Event()

    def run(self):
        while not self.flag.wait(self.interval):
            self.callback()

    def stop(self):
        self.flag.set()
