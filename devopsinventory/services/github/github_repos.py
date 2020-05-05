

import devopsinventory.base.abstract_worker as worker
from devopsinventory.base.abstract_service import Service


class GitHubPuller(worker.Puller):
    """ Example class, to get github repos of an organization"""
    
    @run
    def get_repos(config):
        # TO-DO request, etc.
        # return df
        pass
    



if __name__ == "__main__":
    print('Ejecutando como programa this')
    service = Service(config={})
    service.register(GitHubPuller(config={}))
    service.run()
