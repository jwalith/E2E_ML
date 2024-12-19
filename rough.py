E_DOT = '-e .'
def get_requirements(file_path):
    req=[]
    with open(file_path) as f:
        req = f.read().splitlines()
    print(req)
    if E_DOT in req:
        req.remove(E_DOT)
    return req
    
    
nstall_requires=get_requirements('requirements.txt')
print(nstall_requires)