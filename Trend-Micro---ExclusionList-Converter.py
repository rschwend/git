import re

excl = r"C:\Users\rap\example\Downloads\file.exe|d:\app\my.exe|%windir%\app\azzi.exe"

x = re.split(r'[|]', excl)

for list in x:
    print(list)

