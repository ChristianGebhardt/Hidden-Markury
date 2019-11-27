# -*- coding: utf-8 -*-
"""
Created on Sat Feb 02 09:28:13 2019

@author: LAdmin
"""

### AUXILIARY FUNCTIONS ###
import os                                                                                                             
import platform    

#list all files in directory and all subdirectories
def list_all_files(dir):
    '''
    list all files in directory and all subdirectories      
    '''                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs: 
        if platform.python_version()[0]=="2":                                                                                           
             files = os.walk(subdir).next()[2]
        else:
             files = next(os.walk(subdir))[2]                                                                
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                r.append(subdir + "/" + file)                                                                         
    return r   

def subfolders(dir,foldertag=""):  
    '''
    list folder and all subfolder
    '''     
    r = []   
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:
        if foldertag in subdir:
            r.append(subdir)
    return r

#list folder and all subfolder, which contain specific files (e.g. ".tif" files)
def list_subfolders(dir, filtag):                                                                                                  
    '''
    list folder and all subfolder, which contain specific files (e.g. ".tif" files)
    '''
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        if platform.python_version()[0]=="2":                                                                                           
             files = os.walk(subdir).next()[2]
        else:
             files = next(os.walk(subdir))[2]   
        if (len(files) > 0):
            for file in files:                                                                                        
                if filtag in file:                                                                                      
                    r.append(subdir)
                    break                                                                      
    return r   
 
#list all files in a folder, which have specific tag in filename (e.g. ".tif" or "_apbs_alexa.csv")   
def list_selected_files(dir,tag=None,exclude_tag=None):                                                                                                  
    '''
    list all files in a folder, which have specific tag in filename (e.g. ".tif") and exclude files with a specific tag (e.g. "_meta_data.tif")   
    '''
    r = []                                                                                                                                                                                                     
    if platform.python_version()[0]=="2":                                                                                           
         files = os.walk(dir).next()[2]
    else:
         files = next(os.walk(dir))[2]                                                                               
    if (len(files) > 0):                                                                                          
        for file in files:
            if tag is not None and tag in file:
                if exclude_tag is None or exclude_tag not in file:                                                                                        
                    r.append(os.path.join(dir, file))                                                                         
    return r     

def splitall(path):
    '''
    split file path into list with all subfolders and filename (works for linux and windows paths independent of '/' or '\\')
    '''
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts