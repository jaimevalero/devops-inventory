
from __future__ import print_function
import inventory.devops-inventory.base.abstract_worker

class Service():

    AbstractWorker puller
    AbstractWorker pusher_db
    AbstractWorker pusher_el
    config = {}
    def __init__(self, config):
        self.set_config(config)

    def register(self, tipo, abstractworker):
        if   tipo == 'puller':    self.puller      = abstractworker
        elif tipo == 'pusher_db': self.pusher_db   = abstractworker
        elif tipo == 'pusher_el': self.pusher_else = abstractworker
        else : raise Exception('spam', 'eggs')

    def run(self, tipo, abstractworker):
        puller.run()
        pusher_db.run()
        pusher_el.run()

    def check(self, tipo, abstractworker):
        puller.check()
        pusher_db.check()
        pusher_el.check()

if __name__ == "__main__":
    print('Ejecutando como programa principal')
    sev = Service()

