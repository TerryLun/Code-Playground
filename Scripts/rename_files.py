import os

FILENAME_STARTS = 'WeC'
NAME_LENGTH = 3

count = 1
for file in os.listdir():
    if file.startswith(FILENAME_STARTS):
        os.rename(file, f'{str(count).rjust(NAME_LENGTH, "0")}.png')
        count += 1
