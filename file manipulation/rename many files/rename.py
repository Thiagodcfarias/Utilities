# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:03:00 2020

@author: Thiago D
"""
import glob as g
import os
import random as r

# thins you will need to change
old_path = "" # replace \ to / 
new_path = "" # without last /
extension = '.txt' # with dot
stopwords = ["(",")",extension] # do not remove extension from this list


for file in g.glob(old_path + "/*" + extension):
    
    original_file = file.split('\\')[-1]
    
    file = file.split('\\')[-1]
    
    random_seed = str(r.randint(1,100000))
    
    for char in stopwords:
        file = file.replace(char,'')
    
    file = file.replace(' ', '')
    
    print(file)
    os.rename(old_path + original_file,new_path + "/" + file + random_seed + extension)
