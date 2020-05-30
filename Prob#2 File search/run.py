import json

#################################
###### program methods #######
#################################

def bfs(node,path,target,ls):
    folder = []
    for i in node:
        if (i != "_files"):
            folder.append(i)
        else :
            for j in node[i]:
                if(j==target):
                   output = (path + '/' + target) # for example "\folder1" + "\file1" 
                   ls.append(output)
    
    folder.sort() #sort because case depths of 2 files are equal.
    for i in folder :
        bfs(node[i],path + "/"+ i,target,ls)
        

#################################
###### fileSearch methods #######
#################################

def fileSearch(fileToSearch, filesObj):
    output = [] 
    with open(filesObj) as f:
        data = json.load(f)
    bfs(data,"",fileToSearch,output)

    return output


#############################
###### to run program #######
#############################

print(fileSearch('file1','test.json')) # test find file1 in test.json



