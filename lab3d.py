#!/usr/bin/env python3
'''Lab 3 Part 2 script - check free disk space'''
# Author ID: 160564217

import subprocess

def free_space():

    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = p.communicate()
    

    free_space_str = output[0].decode('utf-8').strip()
    return free_space_str

if __name__ == '__main__':
    print(free_space())
