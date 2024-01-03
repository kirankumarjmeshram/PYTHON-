import os
path = "/home/sarutobi/Downloads/input data/"
folders = os.listdir(path) 
count = 1
for folder in folders:
    old_name = os.path.join(path, folder) 
    new_name = os.path.join(path, f'folder_{count}') 
    os.rename(old_name, new_name) # Rename the folder
    count += 1 
