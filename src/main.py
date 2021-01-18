import yaml
import numpy as np
import pandas as pd
import argparse
from pathlib import Path

"""
File: main.py
Author: yourname
Email: yourname@email.com
Github: https://github.com/yourname
Description:
    [Subject, verb, object,prepositional phase]

    I like spaghetti.
    He reads many books.

"""
def main(myexp_path:str,nr:int)->list:
    ret = [['my exp','niche generator','company ide']]
    # with open("../myexp.txt","r") as f:
    with open(myexp_path,"r") as f:
        myexp = f.readlines()
    with open("../res/object1.dat") as f:
        obj = f.readlines()
    with open("../res/subj.dat","r") as f:
        sub = f.readlines()
    verb = pd.read_csv("../res/verb.dat")
    # print(f"myexp={myexp} len={len(myexp)}")
    # print(f"obj={obj}")
    for ide in range(nr):
        myexp_sel = myexp[np.random.randint(0,len(myexp))].replace("\n","")
        sub_sel = sub[np.random.randint(0,len(sub))].replace("\n","")
        obj_sel = obj[np.random.randint(0,len(obj))].replace(","," ")
        verb_row = np.random.randint(0,verb.shape[0])
        verb_col = verb.keys()[np.random.randint(0,2)]
        verb_sel = verb[verb_col][verb_row].replace("\n","")
        # print(f"{myexp[myexp_sel], obj[obj_sel]}")
        # print(f"{myexp[myexp_sel].replace('\n','')},{verb[verb_col][verb_sel]}, {obj[obj_sel]}")
        # print(f"{myexp_sel}, {verb_sel}, {obj_sel}",end="")
        ret.append([myexp_sel, f"{sub_sel} {verb_sel} {obj_sel}".replace("\n","").replace(","," "),""])

    csvdata = str()
    for item in ret:
        csvdata += f"{item}".replace("[","").replace("]","\n").replace("\'","")

    return csvdata




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
    """
    random ide templet generator

    How to use:

    $python [expfile] [count] [results]\n

    Written by: Magnus Sörensen
    email: btyeofsoren@gmail.com
    """)
    parser.add_argument("myexp",help="Inptu experience file")
    parser.add_argument("count", help="How many items do you want?")
    parser.add_argument("results", help="Output file")
    args = parser.parse_args()
    fmyexp=Path(args.myexp)
    count = int(args.count)
    fresults = args.results

    if fmyexp.exists() and fmyexp.is_file():
        r = main(str(fmyexp),count)

        with open(fresults,"w") as f:
            f.write(r)

