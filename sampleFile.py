import os
import shutil
src1="C:/Users/vasu/Music/python/sample1.txt"
src2="C:/Users/vasu/Music/python/sample2.txt"

with open (src1,"r")as a:
    data_a = a.read()
    
with open (src2,"r")as a:
    data_b = a.read()
    
with open (src2,"w") as a:
    a.write(data_a)

with open (src1,"w") as a:
    a.write(data_b)
    