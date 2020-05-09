from abc import ABCMeta


class AbstractWorker(metaclass=ABCMeta):
    """Clase abstracta del worker, de la que derivan el puller y  el pusher"""
    __config = {}

    def __init__(self,config={}):
        if config != {} : self.set_config(config)
        pass

    def run(func):
        def wrapper(*arg):
            res = func(*arg)
            print ('I\'m a decorator.')
            return res
        return wrapper

    # no more uses of _deco in this class
    run = staticmethod(run)

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

    debug = staticmethod(debug)

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

