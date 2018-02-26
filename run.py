import threading
import itertools
import time


class Loader():
    def __init__(self):
        self.method()


    def method(self):

        def run(self):
            threading.Thread(target=animation, args=(self,)).start()
            gosleep(self)

        def animation(self):
            symbols = itertools.cycle('\\|/-')
            timeout = time.time() + 30

            while timeout > time.time():
                print("\rLoading...{0}".format(next(symbols)), end='')
                time.sleep(0.25)
            print('\r' )

        def gosleep(self):
            time.sleep(30)

        run(self)

Loader()