import threading
from threading import current_thread


class MythreadV2(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')


t1 = MythreadV2()
t1.start()
t1.join()
