# Written by Benjamin Rome 6-6-22
# See README for more info on how to use
import sys
import pandas as pd

if __name__ == "__main__":
    if len(sys.argv) != 2:  
        print("ERROR: Usage: python -3 main.py < my_csv.csv >")
        sys.exit(1)

    CSV  = sys.argv[1]
    data = pd.read_csv(CSV)

    





