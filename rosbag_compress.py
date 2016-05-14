#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import os
import subprocess

def GetBagfilePaths(path):
    u"""
    Get bag file path
    """

    paths=[]
    for filepath in find_all_files(path):
        if ".bag" in filepath:
            paths.append(filepath)
            # print(filepath)

    return paths

def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

def RosbagComressOrDecompress(paths,cmd):
    u"""
    exe rosbag compress or decompress
    """

    for path in paths:
        finalcmd=cmd+path
        print(finalcmd)
        subprocess.Popen(finalcmd,shell=True)

def RemoveOrignalBagFile(paths):
    u"""
    remove original bag files
    """

    for path in paths:
        if ".orig.bag" in path:
            os.remove(path)
            print(path+" is removed!!")

if __name__ == '__main__':

    description=u'This script is a rosbag compress or decompress tool for multiple bag files.\n'

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('-d','--decompress', action='store_true', default=False, help='enable decompress')

    parser.add_argument('-r','--remove', action='store_true', default=False, help='remove original bag file')

    parser.add_argument('-p','--path', type=str, default="./", help='target path')
    args=parser.parse_args()

    paths=GetBagfilePaths(args.path)

    if args.remove:
        RemoveOrignalBagFile(paths)
    elif not args.decompress:#compress
        RosbagComressOrDecompress(paths,"rosbag compress ")
    else:#decompress
        RosbagComressOrDecompress(paths,"rosbag decompress ")

