import os

FILENAME_STARTS = 'WeC'
count = 1
for file in os.listdir():
    if file.startswith(FILENAME_STARTS):
        os.rename(file, f'{str(count).rjust(3, "0")}.png')
        count += 1
