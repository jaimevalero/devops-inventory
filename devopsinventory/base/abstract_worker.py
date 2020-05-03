from abc import ABCMeta


class AbstractWorker(metaclass=ABCMeta):
    """Clase abstracta del worker, de la que derivan el puller y  el pusher"""
    __config = {}

    def __init__(self,config={}):
        if config != {} : self.set_config(config)
        pass

    def set_config(self, config):
        self.config = config

    def get_config(self, config):
        return self.config

    def run(self):
        pass

    def __prerun(self):
        pass

    def __postrun(self):
        pass

    def check(self):
        pass

class Puller(AbstractWorker):
    pass
class Pusher_DB(AbstractWorker):
    pass
class Pusher_EL(AbstractWorker):
    pass

