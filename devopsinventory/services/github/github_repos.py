

import pandas as pd

from devopsinventory.base.abstract_service import Service
from devopsinventory.base.abstract_worker import Puller


class GitHubPuller(Puller):
    pass
    @Puller.run
    def my_funcion(self):
        print("kk")
        return pd.DataFrame()


if __name__ == "__main__":
    print('Ejecutando como programa this')
    sev = Service(config={})
    sev.register(GitHubPuller(config={}))
    sev.run()


