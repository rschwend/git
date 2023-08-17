#Trend-Micro---ExclusionList-Converter

import re

excl = r"C:\Users\rap\example\Downloads\file.exe|d:\app\my.exe|%windir%\app\azzi.exe"
exa = r"C:\Users\rap\example\Downloads\file.exe|d:\app\my.exe|%windir%\app\azzi.exe"
print ("INPUT Example: " + exa)
#excl = str(input())
x = re.split(r'[|]', excl)

for list in x:
    print(list)

