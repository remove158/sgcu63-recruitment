########################
####### input ##########
########################

n,m1,m2 =  input().split()
m1,m2=int(m1),int(m2)

#######################################
##### make floor and split by "." #####
#######################################

floor1 = '''00000.    1.22222.33333.4    4.55555.66666.77777.88888.99999'''.split(".")
floor2 = '''0   0.    1.    2.    3.4    4.5    .6    .    7.8   8.9   9'''.split(".")
floor3 = '''0   0.    1.22222.33333.444444.55555.66666.    7.88888.99999'''.split(".")
floor4 = '''0   0.    1.2    .    3.     4.    5.6   6.    7.8   8.    9'''.split(".")
floor5 = '''00000.    1.22222.33333.     4.55555.66666.    7.88888.99999'''.split(".")

###################################
############# methods #############
###################################

def printf(num,multiple,floor):
    # this method use for print without '\n'  (already multiple)
    for char in floor[num]:
        print(char*multiple,end="")

    print(" "*multiple,end="")   ##indent

def show(char,floor,m2):
    if floor==1:
        printf(int(char),m2,floor1)
    elif floor==2:
        printf(int(char),m2,floor2)
    elif floor==3:
        printf(int(char),m2,floor3)
    elif floor==4:
        printf(int(char),m2,floor4)
    elif floor==5:
        printf(int(char),m2,floor5)


#############################
###### to run program #######
#############################

for floor in range(1,6): # 5 floor
    for repeat in range(m1): ##repeat hight
        for char in n: 
                show(char,floor,m2) 
        print() #for new line


