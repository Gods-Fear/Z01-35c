import os

extension = input(f'Please put a file extension: ')
path = input(f'Please put a path: ')

for file in os.listdir(f"{path}"):
    if file.endswith(f".{extension}"):
        print(os.path.join("path", file))


