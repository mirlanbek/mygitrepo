
from prettytable import PrettyTable

def create_revision_file(result_path):    
    repo_set = bs.RepoSet()
    
    table_repo = []
    table_message = []
    table_sha = []

    for project in repo_set.projects():
        repo = repo_set.repo(project)
        commit = repo.commit()
        message = commit.message.splitlines()[0]
        sha = repo.git.rev_parse(commit.hexsha, short=True)

        table_repo.append(project)
        table_sha.append(sha)
        table_message.append(message)  

    x = PrettyTable()
    x.add_column("Project", [ p for p in table_repo])
    x.add_column("sha", [ s for s in table_sha])
    x.add_column("Message", [ m for m in table_message ])
    
    x.align["Project"] = "l" 
    x.align["Commit"] = "c" 
    x.align["Message"] = "l"  

    with open(result_path+"/revisions.txt", "w") as revs:
        revs.write(str(x))

def cr_table():    
    
    from prettytable import PrettyTable
    x = PrettyTable() 
    x.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"]) 
    x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386]) 
    x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769]) 
    x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])

    print(x)
    # with open("/tmp/revisions.txt", "w") as revs:
    #     revs.write(str(x)) 

cr_table()

