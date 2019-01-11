''' this module is to create ticks and check proper time differences '''
import time


class Ticker:
    '''this is used to create a time ticks'''

    def __init__(self, delta):
        self.time = time.time()
        self.delta = delta

    def get(self):
        '''when ticker is called'''
        time_difference = (time.time() - self.time)
        if time_difference > self.delta:
            self.time = time.time()
        return time_difference
