import json
import argparse

"""cli"""
modify_parser = argparse.ArgumentParser(description="to modify values")
modify_parser.add_argument("Deletekey", metavar="Deletekey", type=str, help="What to change")
modify_parser.add_argument("tochange", metavar="tochange", type=str, help="thing to be changed to")
args = modify_parser.parse_args()

Deletekey = args.Deletekey
tochange = args.tochange
'''cli'''

import os
Type = "Projects"
os.chdir(f"C:/DEV/Projects/{Type}")
with open("Storeviol.json","r+") as f:
    vio = f.readlines()
global e
for i in vio:
    for e in i:
        e = dict(e)

e["name"] = "vc"
with open("Storeviolin.json",'w') as f:
    f.write(f"{vio}")
