import os
# 

# get curret directory:
def current_dir():
    cd = os.getcwd()
    print("this is current directory :",cd)

# changing the current directory :
def change_dir(path):
    os.chdir(path) # go one directory back. => path = '/'


# create a directory => os.mkdir(path,your_new_directory_name) :
 # 1- the directory you wanna create folder in .=> location = 'G:/codes/shitcodes/python/os_module'
 # 2- name your directory . => file_name = 'new_file'
 # 3- create the path .=> os.path.join(location,file_name)
 # 4- create DIRECTORY .
def create_dir(location,file_name):
    path = os.path.join(location,file_name)       
    os.mkdir(path)                                      

# list directories :
 # 1- path = 'c:/'
def list_dir(path):
    dir_list = os.listdir(path) 

# delete a file or directory :
def delete_file(location,file_name):
    path = os.path.join(location,file_name)
    os.remove(path)

def delete_dir(location,dir_name):
    path = os.path.join(location,dir_name)
    os.rmdir(path)

# 
