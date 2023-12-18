import os

count = 0
dir_path = r'basic'
for path in os.scandir(dir_path):
    if path.is_file():
        count += 1
print('file count:', count)