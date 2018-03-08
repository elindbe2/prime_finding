import time

class Timer(object):
    def __init__(self, msg):
        self.msg = msg

    def __enter__(self):
        self.start = time.clock()

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start
        print('{msg}: {interval}'.format(msg=self.msg, interval=self.interval))
