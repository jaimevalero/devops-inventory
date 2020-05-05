
from __future__ import print_function

import time

import devopsinventory.base.abstract_worker as worker
from devopsinventory.base.abstract_worker import AbstractWorker


class Service():
    """ Class that represents the inventory process of a CI.
    Its a composite of 3 workers, that performs the push and pull of the CI info"""
    
    # Objeto que saca la info de la plataforma externa (github, AD, ....)
    puller: AbstractWorker
    # Objeto que inserta la info extraida en BD SQL (mysql por defecto)
    pusher_db: AbstractWorker
     # Objeto que inserta la info extraida en BD no SQL (EL por defecto)
    pusher_el: AbstractWorker
    # Configuracion con endpoint y credentials    
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
        print("worker ")

        if   isinstance(worker, worker.Puller)    :
            print("Registramos Puller ")
            self.puller    = worker
        elif isinstance(worker, worker.Pusher_DB) :
            print("Registramos Pusher_DB ")
            self.pusher_db = worker
        elif isinstance(worker, worker.Pusher_EL) :
            print("Registramos Pusher_EL ")
            self.pusher_el = worker
        else :
            print("No hemos encontrado el tipo de  ", worker)
            raise Exception('spam', 'eggs')

    def run(self ):
        puller.run()
        pusher_db.run()
        pusher_el.run()

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
