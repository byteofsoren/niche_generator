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
    with open("../res/pregen.dat","r") as f:
        pregen = f.readlines()

    for ide in range(nr):
        myexp_sel = myexp[np.random.randint(0,len(myexp))].replace("\n","")
        pregen_sel = pregen[np.random.randint(0,len(pregen))].replace(","," ").replace("\n","")
        # ret.append([myexp_sel, f"{sub_sel} {verb_sel} {obj_sel}".replace("\n","").replace(","," "),""])
        ret.append([myexp_sel, pregen_sel, ""])


    csvdata = str()
    for item in ret:
        csvdata += f"{item}".replace("[","").replace("]","\n").replace("\'","")

    return csvdata




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
    """
    Pregenerated templet is used to create random niches.

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

