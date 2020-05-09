
from __future__ import print_function

import time

import devopsinventory.base.abstract_worker as worker
import devopsinventory.base.utilities
from devopsinventory.base.abstract_worker import AbstractWorker


class Service():

    puller: AbstractWorker
    pusher_db: AbstractWorker
    pusher_el: AbstractWorker
    config = {}

    def debug(func):
        print(f"{func.__name__!r} begins")
        start_time = time.time()

        def inner(*args, **kwargs):
            print(f"""f Arguments for args: {args}""")
            print(f"""f Arguments for kwargs: {kwargs}""")
            return func(*args, **kwargs)

        results = inner
        print(f"{func.__name__!r} ends in {time.time() - start_time}  secs")
        return results

    @debug
    def set_config(self, config):
        """  Refresh config"""
        self.config = config
        self.puller.set_config( self.config )
        self.pusher_db.set_config(self.config)
        self.pusher_el.set_config(self.config)


    def __init__(self, config={}):

        self.puller = worker.Puller(config)
        self.pusher_db = worker.Pusher_DB(config)
        self.pusher_el = worker.Pusher_EL(config)
        self.set_config(config)

    @debug
    def register(self,  worker ):

        if   isinstance(worker , ( devopsinventory.base.abstract_worker.Puller)) :
            print("Registramos Puller ")
            self.puller = worker
        elif isinstance(worker , ( devopsinventory.base.abstract_worker.Pusher_DB)) :
            print("Registramos Pusher_DB ")
            self.pusher_db = worker
        elif isinstance(worker , ( devopsinventory.base.abstract_worker.Pusher_EL)) :
            print("Registramos Pusher_EL ")
            self.pusher_el = worker
        else :
            print("No hemos encontrado el tipo de  ", worker)
            raise Exception('spam', 'eggs')

    @debug
    def run(self ):
        self.puller.run()
        self.pusher_db.run()
        self.pusher_el.run()

    def check(self):
        puller.check()
        pusher_db.check()
        pusher_el.check()


"""if __name__ == "__main__":
    config = { "1" : 2 }
    print('Ejecutando como programa principal')
    sev = Service(config=config)
    #sev.run()
"""