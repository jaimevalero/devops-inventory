

import devopsinventory.base.abstract_worker as worker
from devopsinventory.base.abstract_service import Service


class GitHubPuller(worker.Puller):
    pass
    #def register(self, worker):



if __name__ == "__main__":
    print('Ejecutando como programa this')
    sev = Service(config={})
    sev.register(GitHubPuller(config={}))
