import json


def bfs(node,path,target,ls):
    folder = []
    for i in node:
        if (i != "_files"):
            folder.append(i)
        else :
            for j in node[i]:
                if(j==target):
                   output = (path + '/' + target)
                   ls.append(output)
    
    folder.sort()
    for i in folder :
        bfs(node[i],path + "/"+ i,target,ls)


def fileSearch(fileToSearch, filesObj):
    output = [] 
    with open(filesObj) as f:
        data = json.load(f)
    bfs(data,"",fileToSearch,output)

    return output



print(fileSearch('file1','test.json'))



